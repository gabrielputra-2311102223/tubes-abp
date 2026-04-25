import sqlite3

# Membuat file database (akan otomatis terbuat jika belum ada)
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# 1. Buat Tabel Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# 2. Buat Tabel Motors
cursor.execute('''
CREATE TABLE IF NOT EXISTS motors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL,
    harga INTEGER NOT NULL,
    status TEXT DEFAULT 'available'
)
''')

# 3. Masukkan Data Admin sebagai percobaan awal
try:
    cursor.execute("INSERT INTO users (nama, email, password, role) VALUES ('Administrator', 'admin@gmail.com', 'admin123', 'admin')")
except sqlite3.IntegrityError:
    pass # Abaikan jika admin sudah ada

connection.commit()
connection.close()

print("Mantap! Database database.db beserta tabelnya berhasil dibuat!")