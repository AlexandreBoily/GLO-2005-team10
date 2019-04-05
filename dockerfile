# Partir de l’image officielle de Python 3.7
FROM python:3.7-slim

# Mettre le code de l’application dans le répertoire /code de l’image
WORKDIR /code

# Copier les librairie nécessaire à votre application
ADD requirements.txt /code

# Installer les packages Python nécessaires dans requirements.txt
RUN pip install -r requirements.txt

# Copier le code de l’application dans le répertoire /
ADD . /code

#Exposer les ports 8080 et 3306
EXPOSE 8080


# Lancer le script app.py quand le container démarre
CMD ["python","app.py"]