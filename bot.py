import os
import requests
import time
from telegram import Bot

# Configura il bot con le variabili d'ambiente
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=TOKEN)

# Funzione per ottenere offerte Amazon (da personalizzare con una vera API)
def get_amazon_offers():
    url = "https://example.com/api/offerte"  # Cambia con un'API reale
    try:
        response = requests.get(url)
        offers = response.json()[:5]  # Prendi le prime 5 offerte
        return offers
    except:
        return []

# Loop per inviare offerte ogni ora
while True:
    offers = get_amazon_offers()
    for offer in offers:
        message = f"📢 {offer['title']}\n💰 Prezzo: {offer['price']}\n🔗 {offer['link']}"
        bot.send_message(chat_id=CHAT_ID, text=message)
    time.sleep(3600)  # Aspetta un'ora prima di inviare nuove offerte
