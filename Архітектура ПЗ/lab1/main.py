import sqlite3
from datetime import datetime


class DatabaseHandler:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self._connect()

    def _connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT,
            hired_date TEXT
        )''')
        self.conn.commit()

    def add_employee(self, name, department):
        hired_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO employees (name, department, hired_date) VALUES (?, ?, ?)",
                            (name, department, hired_date))
        self.conn.commit()

    def get_employee(self, emp_id):
        self.cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
        return self.cursor.fetchone()

    def get_all_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()

    def clone_employee(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.add_employee(emp[1], emp[2])

    def add_department(self, emp_id, new_department):
        self.cursor.execute("UPDATE employees SET department = ? WHERE id = ?", (new_department, emp_id))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


# Приклад використання
if __name__ == "__main__":
    db = DatabaseHandler()
    db.add_employee("John Doe", "IT")
    db.add_employee("Jane Smith", "HR")

    print("Всі працівники:", db.get_all_employees())
    db.clone_employee(1)
    print("Після клонування:", db.get_all_employees())

    db.add_department(2, "Finance")
    print("Оновлені дані:", db.get_all_employees())

    db.close_connection()
