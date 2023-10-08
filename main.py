import os
from dotenv import load_dotenv
from openia import get_ia_response
from fastapi import FastAPI, HTTPException, Request
from whatsapp import extract_whatsapp_received_message, extract_whatsapp_received_number, send_whatsapp_message

WHATSAPP_VERIFY_TOKEN = os.getenv('WHATSAPP_VERIFY_TOKEN')

load_dotenv()

app = FastAPI()


@app.get('/whatsapp-business/webhook')
def verify_facebook_webhook(request: Request):
    challenge = request.query_params.get('hub.challenge')
    verify_token = request.query_params.get('hub.verify_token')

    if not verify_token == WHATSAPP_VERIFY_TOKEN:
        raise HTTPException(
            status_code=403, detail="Invalid verification token")

    return int(challenge)


@app.post('/whatsapp-business/webhook')
async def receive_whatsapp_webhook(request: Request):
    request_json = await request.json()

    received_message = extract_whatsapp_received_message(request_json)
    received_number = extract_whatsapp_received_number(request_json)

    if received_message:
        ia_response = get_ia_response(received_message)

        send_whatsapp_message(ia_response, received_number)
