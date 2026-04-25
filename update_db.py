import sqlite3

# Membuka brankas database yang sudah ada
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Membuat laci (tabel) khusus untuk pesanan
cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    nama_penyewa TEXT NOT NULL,
    motor_id INTEGER NOT NULL,
    nama_motor TEXT NOT NULL,
    tgl_mulai DATE NOT NULL,
    tgl_selesai DATE NOT NULL,
    total_harga INTEGER NOT NULL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

connection.commit()
connection.close()

print("Mantap! Tabel 'bookings' berhasil ditambahkan ke database!")