from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def home():
    return render_template('crypto.html')

# Traitement du chiffrement
@app.route('/encrypt-form', methods=['POST'])
def encrypt_message():
    key = request.form.get('key')
    message = request.form.get('message')

    try:
        cipher = Fernet(key.encode())
        encrypted_message = cipher.encrypt(message.encode()).decode()
        result = f"Message chiffré : {encrypted_message}"
    except Exception as error:
        result = f"Erreur : {str(error)}"

    return render_template('crypto.html', result=result)

# Traitement du déchiffrement
@app.route('/decrypt-form', methods=['POST'])
def decrypt_message():
    key = request.form.get('key')
    encrypted_message = request.form.get('message')

    try:
        cipher = Fernet(key.encode())
        decrypted_message = cipher.decrypt(encrypted_message.encode()).decode()
        result = f"Message déchiffré : {decrypted_message}"
    except Exception as error:
        result = f"Erreur : {str(error)}"

    return render_template('crypto.html', result=result)

# Génération d'une nouvelle clé
@app.route('/generate-key/')
def generate_key():
    new_key = Fernet.generate_key().decode()
    return {'key': new_key}

if __name__ == '__main__':
    app.run(debug=True)
