# Utiliser une image Python légère
FROM python:3.11

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposer le port Heroku
EXPOSE $PORT

# Commande pour exécuter Flask avec Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:$PORT", "app:app"]
