# Utiliser l'image officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel l'application va tourner
EXPOSE $PORT

# Démarrer l'application avec Gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
