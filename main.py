from dotenv import load_dotenv
from openia import get_ia_response
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from whatsapp import extract_whatsapp_received_message, extract_whatsapp_received_number, send_whatsapp_message

load_dotenv()

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post('/whatsapp-business/webhook')
async def receive_whatsapp_webhook(request: Request):
    request_json = await request.json()

    received_message = extract_whatsapp_received_message(request_json)
    received_number = extract_whatsapp_received_number(request_json)

    if received_message:
        ia_response = get_ia_response(received_message)

        send_whatsapp_message(ia_response, received_number)


@app.get('/politica-de-privacidade', response_class=HTMLResponse)
def politica_de_privacidade():
    return open("static/politica_de_privacidade.html").read()
