from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route GET de chiffrement avec clé fournie en paramètre (Exercice 2)
@app.route('/encrypt/', methods=['POST'])
def encryptage():
    data = request.get_json()
    valeur = data.get('message')
    user_key = data.get('key')

    if not valeur or not user_key:
        return jsonify({'error': 'Message et clé sont requis'}), 400

    try:
        f = Fernet(user_key.encode())
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return jsonify({'encrypted_message': token.decode()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route POST de déchiffrement avec clé fournie (Exercice 1 & 2)
@app.route('/decrypt/', methods=['POST'])
def decryptage():
    data = request.get_json()
    token = data.get('message')
    user_key = data.get('key')

    if not token or not user_key:
        return jsonify({'error': 'Message et clé sont requis'}), 400

    try:
        f = Fernet(user_key.encode())
        valeur = f.decrypt(token.encode()).decode()
        return jsonify({'decrypted_message': valeur})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route utilitaire pour générer une clé Fernet
@app.route('/generate-key/')
def generate_key():
    return jsonify({'key': Fernet.generate_key().decode()})

if __name__ == "__main__":
    app.run(debug=True)
