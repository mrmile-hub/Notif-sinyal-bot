import requests
import time
import os

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

def job():
    send_telegram_message("🚨 Sinyal Entry LONG PENGU/USDT\nEntry: 0.0389\nTP: 0.0410\nSL: 0.0378")

if __name__ == "__main__":
    while True:
        job()
        time.sleep(3600)
