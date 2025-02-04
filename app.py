from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import mysql.connector
import nltk
from keras.models import load_model
import numpy as np
import json
import random
import pickle


# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
try:
    db = mysql.connector.connect(
        host="localhost",
        port="3307",
        user="root",
        password="",
        database="user_data"
    )
    cursor = db.cursor()
except mysql.connector.Error as err:
    print(f"Database connection error: {err}")
    db = None
    cursor = None

# Load chatbot model and supporting files
try:
    model = load_model('chatbot_model.h5')
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    with open('intents.json') as file:
        intents_json = json.load(file)
except FileNotFoundError as e:
    print(f"File not found: {e}")
    model, words, classes, intents_json = None, None, None, None
except Exception as e:
    print(f"Error loading resources: {e}")
    model, words, classes, intents_json = None, None, None, None

lemmatizer = nltk.stem.WordNetLemmatizer()

def preprocess_input(sentence):
    try:
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        bag = [1 if word in sentence_words else 0 for word in words]
        return np.array(bag)
    except Exception as e:
        print(f"Error in preprocessing input: {e}")
        return np.zeros(len(words))

def predict_class(sentence):
    if model is None or words is None or classes is None:
        print("Model or resources not loaded properly.")
        return []
    try:
        input_data = preprocess_input(sentence)
        input_data = np.expand_dims(input_data, axis=0)
        predictions = model.predict(input_data)[0]
        threshold = 0.25
        results = [[i, p] for i, p in enumerate(predictions) if p > threshold]
        results.sort(key=lambda x: x[1], reverse=True)
        return [{"intent": classes[r[0]], "probability": str(r[1])} for r in results]
    except Exception as e:
        print(f"Error in predicting class: {e}")
        return []

def get_response(intents_list, intents_json):
    if not intents_list:
        return "I don't understand."
    tag = intents_list[0]['intent']
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I don't understand."

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()
    if user:
        session['user_email'] = email  # Set session for logged-in user
        flash("Login successful!", "success")
        return redirect(url_for('chatbot'))
    else:
        flash("Invalid email or password!", "danger")
        return redirect(url_for('login_page'))



@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirmpass = request.form['confirmpass']
    if password != confirmpass:
        flash("Passwords do not match!", "danger")
        return redirect(url_for('home'))
    if cursor is None:
        flash("Database connection is unavailable!", "danger")
        return redirect(url_for('home'))
    try:
        query = "INSERT INTO users (name, email, password, confirmpass) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, password, confirmpass))
        db.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login_page'))
    except mysql.connector.IntegrityError:
        flash("Email already exists!", "danger")
        return redirect(url_for('home'))
    except Exception as e:
        flash(f"An error occurred during registration: {e}", "danger")
        return redirect(url_for('home'))


@app.route('/bot')
def chatbot():
    return render_template('bot.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data['message']
        user_email = session.get('user_email')  # Retrieve user email from session

        if not user_email:
            return jsonify({"error": "User not logged in"}), 401

        # Get user_id from the database
        cursor.execute("SELECT id FROM users WHERE email = %s", (user_email,))
        user = cursor.fetchone()
        if not user:
            return jsonify({"error": "User not found"}), 404

        user_id = user[0]

        # Predict chatbot response
        intents = predict_class(message)
        response = get_response(intents, intents_json)

        # Save chat history
        query = """
            INSERT INTO chat_history (user_id, user_message, bot_response) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (user_id, message, response))
        db.commit()

        return jsonify({"response": response})
    except Exception as e:
        print(f"Error during chat processing: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8012)
