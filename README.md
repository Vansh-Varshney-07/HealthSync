This is a basic AI-powered health chatbot designed to assist users by providing advice based on their symptoms. It uses WhatsApp API (via Twilio) and Flask for the backend. The AI logic uses simple symptom-based responses.

- Symptom-based diagnosis
- WhatsApp integration
- Simple AI response using predefined symptom-condition mapping

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/whatsapp-health-bot.git
    cd whatsapp-health-bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Twilio (WhatsApp API):
   - Follow [Twilio’s WhatsApp setup guide](https://www.twilio.com/docs/whatsapp).
   - Get your **Account SID** and **Auth Token** from Twilio.

4. Run the server:
    ```bash
    python app.py
    ```

5. Test the bot by sending a message to your Twilio WhatsApp number.
