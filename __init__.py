from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('crypto.html')

@app.route('/encrypt-form', methods=['POST'])
def encrypt_form():
    key = request.form['key']
    message = request.form['message']

    try:
        f = Fernet(key.encode())
        encrypted = f.encrypt(message.encode()).decode()
        return render_template('crypto.html', result=f"Message chiffré : {encrypted}")
    except Exception as e:
        return render_template('crypto.html', result=f"Erreur : {str(e)}")

@app.route('/decrypt-form', methods=['POST'])
def decrypt_form():
    key = request.form['key']
    message = request.form['message']

    try:
        f = Fernet(key.encode())
        decrypted = f.decrypt(message.encode()).decode()
        return render_template('crypto.html', result=f"Message déchiffré : {decrypted}")
    except Exception as e:
        return render_template('crypto.html', result=f"Erreur : {str(e)}")

# Bonus : route pour générer une clé
@app.route('/generate-key/')
def generate_key():
    return {'key': Fernet.generate_key().decode()}

if __name__ == '__main__':
    app.run(debug=True)
