import os
import requests
import time
import logging
from telegram import Bot

# Configura il logging per debug
logging.basicConfig(level=logging.INFO)

# Configura il bot con le variabili d'ambiente
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=TOKEN)

# Funzione per ottenere offerte Amazon (da personalizzare con un'API reale)
def get_amazon_offers():
    return [
        {"title": "Prodotto 1", "price": "19.99€", "link": "https://amazon.it/prodotto1"},
        {"title": "Prodotto 2", "price": "29.99€", "link": "https://amazon.it/prodotto2"},
    ]

# Loop per inviare offerte ogni ora
while True:
    offers = get_amazon_offers()
    for offer in offers:
        message = f"📢 {offer['title']}\n💰 Prezzo: {offer['price']}\n🔗 {offer['link']}"
        bot.send_message(chat_id=CHAT_ID, text=message)
        time.sleep(5)  # Evita di mandare troppi messaggi in una volta
    logging.info("Aspetto un'ora prima del prossimo invio...")
    time.sleep(3600)  # Aspetta un'ora prima di inviare nuove offerte