import os
import requests

WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN')
WHATSAPP_API_VERSION = os.getenv('WHATSAPP_API_VERSION')
WHATSAPP_VERIFY_TOKEN = os.getenv('WHATSAPP_VERIFY_TOKEN')
WHATSAPP_SENDER_NUMBER = os.getenv('WHATSAPP_SENDER_NUMBER')
WHATSAPP_RECEIVER_NUMBER = os.getenv('WHATSAPP_RECEIVER_NUMBER')


def send_whatsapp_message(text_response, received_number):
    url = f"https://graph.facebook.com/{WHATSAPP_API_VERSION}/{WHATSAPP_SENDER_NUMBER}/messages"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {WHATSAPP_TOKEN}'
    }
    data = {
        "to": received_number,
        "messaging_product": "whatsapp",
        "type": "text",
        "text": {
            "body": text_response
        }
    }

    response = requests.post(url, json=data, headers=headers)

    pass


def extract_whatsapp_received_message(message):
    content = message['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    return content


def extract_whatsapp_received_number(message):
    number = message['entry'][0]['changes'][0]['value']['messages'][0]['from']
    return number
