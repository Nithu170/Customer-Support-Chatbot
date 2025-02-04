**1.Project Overview:**
The Customer Support Chatbot is an intelligent system designed to assist users by answering queries automatically. It leverages Natural Language Processing (NLP) and Machine Learning (ML) to provide accurate responses and improve customer interactions.
 
**2.Features:**
✅ Real-time customer support with AI-driven responses
✅ User-friendly UI with a smooth chatbot experience
✅ NLP-powered query understanding using NLTK
✅ Database integration for storing and retrieving queries
✅ Hybrid backend using PHP (XAMPP) & Python (Flask/Django)

**3.Tech Stack:**
**📌 Frontend:**
HTML, CSS, React.js (User Interface)

**📌 Backend:**
PHP with XAMPP (Handles API requests, stores chatbot interactions)
Flask/Django (Python) (Handles ML model execution & NLP processing)

**📌 Machine Learning & NLP:**
TensorFlow & Keras (ML model implementation)
Scikit-learn (Training & evaluation)
NLTK (Natural Language Toolkit) (Text preprocessing & query handling)
Pandas (Data processing)

**📂 Project Structure:**

📁 Customer-Support-Chatbot  
│── 📂 frontend/             # React.js UI  
│── 📂 backend/              # Flask/Django API  
│── 📂 php-backend/          # PHP (XAMPP)  
│── 📂 models/               # Trained ML model  
│── 📂 data/                 # Chatbot dataset  
│── 📄 requirements.txt      # Python dependencies  
│── 📄 README.md             # Project Documentation  
**4. Installation & Setup:**
🔹 Step 1: Clone the Repository
git clone https://github.com/Nithu170/Customer-Support-Chatbot.git
cd Customer-Support-Chatbot

🔹 Step 2: Backend Setup (PHP & XAMPP)
Install XAMPP from Apache Friends.
Move the php-backend folder to XAMPP’s htdocs directory:
C:\xampp\htdocs\customer-support-chatbot

Start Apache & MySQL from the XAMPP Control Panel.
Open phpMyAdmin and create a database:

CREATE DATABASE chatbot_db:

Import database.sql file (provided in the php-backend folder).

🔹 Step 3: Backend Setup (Flask/Django + ML Model)
(A) Install Dependencies (Python)

pip install -r requirements.txt
(B) Run the Backend Server (Flask/Django)
If using Flask, run:

python backend/app.py
If using Django, run:

python manage.py runserver
🔹 Step 4: Run the Frontend (React.js)

cd frontend
npm install
npm start

🔹 Step 5: Test the Chatbot
Open http://localhost:3000/ in your browser.
Start a conversation with the chatbot! 🎉

**5.Future Enhancements:**

✔ Improve chatbot accuracy with deep learning models (Transformers, BERT).
✔ Deploy using Docker & Kubernetes for scalability.
✔ Add speech-to-text & text-to-speech for voice interactions.
✔ Implement multi-language support for global users.
