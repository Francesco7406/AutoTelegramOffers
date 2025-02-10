# Usa l'immagine Python ufficiale
FROM python:3.9

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file del bot
COPY bot.py .
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Comando per avviare il bot
CMD ["python", "bot.py"]