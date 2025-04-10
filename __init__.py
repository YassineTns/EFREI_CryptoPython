from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Génération de la clé et création d'un objet Fernet
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Chiffrement
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token chiffré

if __name__ == "__main__":
    app.run(debug=True)
