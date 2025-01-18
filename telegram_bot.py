import requests
from config import TELEGRAM_BOT_TOKEN

bot_token = TELEGRAM_BOT_TOKEN

def send_telegram_message(chat_id, message):
    """Sends a message to the specified Telegram chat ID."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}

    response = requests.post(url, data=data)

    print(response.json())  # Check response for errors

if __name__ == '__main__':
    # Replace with your actual Telegram chat ID to test
    test_chat_id = "7575529318" 
    test_message = "This is a test message from the price alert bot!"
    send_telegram_message(test_chat_id, test_message)