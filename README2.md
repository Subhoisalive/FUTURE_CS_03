from flask import Flask, request, render_template, send_file
import os
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DECRYPT_FOLDER = 'decrypted'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    data = uploaded_file.read()
    encrypted_data = encrypt_file(data)

    encrypted_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename + '.enc')
    with open(encrypted_path, 'wb') as f:
        f.write(encrypted_data)

    return f"✅ File encrypted and saved as {uploaded_file.filename}.enc"

@app.route('/download/<filename>')
def download(filename):
    enc_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(enc_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_file(encrypted_data)
    dec_path = os.path.join(DECRYPT_FOLDER, filename.replace('.enc', ''))
    with open(dec_path, 'wb') as f:
        f.write(decrypted_data)

    return send_file(dec_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
