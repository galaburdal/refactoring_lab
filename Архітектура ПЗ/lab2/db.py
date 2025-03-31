import sqlite3
import bcrypt
from datetime import datetime

class Database:
    def __init__(self, db_name='bike_shop.db'):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            password TEXT NOT NULL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            bike_type TEXT NOT NULL,
            price REAL NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )''')

        self.connection.commit()

    def add_user(self, name, email, phone, password):
        try:
            self.cursor.execute("INSERT INTO users (username, email, phone, password) VALUES (?, ?, ?, ?)",
                                (name, email, phone, password))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def add_order(self, user_id, bike_type, price):
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.cursor.execute(
                "INSERT INTO orders (user_id, bike_type, price, order_date) VALUES (?, ?, ?, ?)",
                (user_id, bike_type, price, order_date),
            )
            self.connection.commit()
            return True
        except Exception:
            return False
