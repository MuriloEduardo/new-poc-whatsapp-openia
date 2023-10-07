from dotenv import load_dotenv
from openia import get_ia_response
from fastapi import FastAPI, Request
from whatsapp import extract_whatsapp_received_message, extract_whatsapp_received_number, send_whatsapp_message

load_dotenv()

app = FastAPI()


@app.post('/whatsapp-business/webhook')
async def receive_whatsapp_webhook(request: Request):
    # Recebe mensagem vinda do whatsapp
    request_json = await request.json()
    received_message = extract_whatsapp_received_message(request_json)
    received_number = extract_whatsapp_received_number(request_json)

    # Envia essa mensagem para a OpenAI
    ia_response = get_ia_response(received_message)

    # Envie uma nova mensagem para o whatsapp
    send_whatsapp_message(ia_response, received_number)
    pass
