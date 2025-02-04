import pickle

# Updated vocabulary with relevant words (extended to 102 words)
updated_words = [
    'available', 'camera', 'cost', 'detail', 'does', 'feature', 'for', 
    'have', 'headphone', 'highlight', 'how', 'include', 'in', 'is', 
    'it', 'large', 'lightweight', 'laptop', 'life', 'long', 'much', 
    'now', 'of', 'price', 'processor', 'purchase', 'smartphone', 
    'stock', 'storage', 'tell', 'the', 'touchscreen', 'what', 
    'wireless', 'you', 'greeting', 'hello', 'hi', 'hey', 'bye', 'goodbye',
    'thanks', 'appreciate', 'order', 'status', 'track', 'shipping', 
    'arrival', 'update', 'return', 'refund', 'policy', 'cancel', 
    'modify', 'item', 'device', 'account', 'password', 'reset', 'access',
    'help', 'technical', 'issue', 'error', 'change', 'address', 'payment',
    'method', 'time', 'shipping', 'method', 'international', 'delivered',
    'receive', 'order', 'modification', 'order_status', 'order_tracking',
    'warranty', 'discount', 'offer', 'price_range', 'payment_options', 
    'shipping_time', 'model', 'brand', 'customer', 'feedback', 'review', 
    'rating', 'support', 'resolution', 'order_id', 'tracking_number', 
    'delivery', 'return_policy', 'exchange', 'invoice', 'transaction', 
    'confirmation', 'bill', 'checkout', 'availability', 'shipment'
]

# Update words.pkl
try:
    # Save the updated word list to words.pkl
    with open('words.pkl', 'wb') as f:
        pickle.dump(updated_words, f)
    
    # Load the words from words.pkl to check the content
    with open('words.pkl', 'rb') as f:
        words = pickle.load(f)
        print(f"Number of words in words.pkl: {len(words)}")
        print(f"First 20 words: {words[:20]}")  # Display first 20 words to verify
    
    print("words.pkl has been updated successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
