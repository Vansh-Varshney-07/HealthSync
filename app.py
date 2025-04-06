from flask import Flask, request, jsonify
import json
import os
from ai_logic import process_symptoms  # Import AI logic for symptom processing

app = Flask(__name__)

# Dummy data for testing (Could be expanded with a real database)
users = {}

# API to send a message from WhatsApp
@app.route('/webhook', methods=['POST'])
def webhook():
    # Extract incoming data (from Twilio/WhatsApp API)
    incoming_message = request.json.get('Body', '').lower()
    from_number = request.json.get('From')

    # Process the incoming message and get AI-based reply
    reply = process_symptoms(incoming_message)

    # Return the response to WhatsApp (Twilio)
    return jsonify({
        'status': 'success',
        'message': reply
    })

@app.route('/send_message', methods=['POST'])
def send_message():
    """API to simulate sending messages from the chatbot to users."""
    user_message = request.json.get('message', '')
    user_number = request.json.get('number')

    # Simulate sending a reply (call the AI logic function)
    response = process_symptoms(user_message)

    return jsonify({
        'status': 'success',
        'response': response
    })

# Home page route
@app.route('/')
def index():
    return "WhatsApp Health Chatbot API Running!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
