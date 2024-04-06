import requests

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    return response.json()

TOKEN = "7045613534:AAEtUDmdb8mApk-ym_3tnbjhLjw1x7LyuJg"
CHAT_ID = 6388674146
MESSAGE = "Halo, ini adalah pesan dari bot Anda!"

send_message(TOKEN, CHAT_ID, MESSAGE)
