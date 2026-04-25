import os
import sqlite3
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_url_path='/assets', static_folder='assets')
CORS(app)

# Ambil jalur folder saat ini secara otomatis
base_dir = os.path.dirname(os.path.abspath(__file__))

def get_db_connection():
    conn = sqlite3.connect(os.path.join(base_dir, 'database.db'))
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return send_from_directory(base_dir, 'index.html')

@app.route('/login.html')
def login():
    # Menggunakan base_dir agar pencarian file lebih akurat
    return send_from_directory(base_dir, 'login.html')

@app.route('/register.html')
def register_page():
    return send_from_directory(base_dir, 'register.html')

# --- DIAGNOSTIK: Cek apakah file ada ---
@app.route('/cek-file')
def cek_file():
    files = os.listdir(base_dir)
    ada = "login.html" in files
    return f"Daftar file di folder: {files} <br> Apakah login.html ada? {'ADA' if ada else 'TIDAK ADA'}"

# ... (sisakan kode API register/login kamu di bawah sini) ...

if __name__ == '__main__':
    app.run(debug=True)