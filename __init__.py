from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Génération d'une clé pour Fernet
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route pour chiffrer une valeur avec Fernet
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Fonction de déchiffrement César
def cesar_dechiffre(text, key):
    result = ""
    for c in text:
        if c.isalpha():
            shift = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - shift - key) % 26 + shift)
        else:
            result += c
    return result

# Route pour décrypter un texte chiffré avec César via force brute
@app.route('/decrypt/')
def decrypt():
    texte_chiffre = request.args.get('text')  # Exemple : /decrypt/?text=Khoor Zruog
    if not texte_chiffre:
        return jsonify({"error": "Paramètre 'text' requis."}), 400

    resultats = {}
    for key in range(1, 26):
        resultats[f"clé_{key}"] = cesar_dechiffre(texte_chiffre, key)

    return jsonify(resultats)

if __name__ == "__main__":
    app.run(debug=True)
