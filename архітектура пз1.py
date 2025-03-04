from abc import ABC, abstractmethod
from bson import ObjectId
import openpyxl
import sqlite3
import matplotlib.pyplot as plt
from pymongo import MongoClient

from Config import connection_string_mongo

# Абстрактний клас для підключення до бази даних
class DBConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch_manager(self):
        pass

    @abstractmethod
    def fetch_workers(self):
        pass

    @abstractmethod
    def duplicate_workers(self):
        pass

# Реалізація підключення до MongoDB
class MongoConnector(DBConnection):
    def connect(self):
        try:
            client = MongoClient(connection_string_mongo)
            database = client['CompanyDB']
            return database
        except Exception as err:
            print(f"Помилка підключення до MongoDB: {err}")
            return None

    def fetch_manager(self):
        db = self.connect()
        collection = db['Employees']
        record = collection.find_one()
        if record:
            record.pop('_id', None)
        return record

    def fetch_workers(self):
        db = self.connect()
        return db['Employees'].find()

    def duplicate_workers(self):
        db = self.connect()
        collection = db['Employees']
        manager = self.fetch_manager()
        first_names = ['Alex', 'Emma', 'Liam', 'Sophia']
        last_names = ['Brown', 'Taylor', 'White', 'Clark']
        skills_management = [['Leadership', 'Planning', 'Negotiation'],
                             ['Strategy', 'Coordination', 'Time Management'],
                             ['Decision Making', 'Organization', 'Supervision']]
        skills_tech = [['Coding', 'Networking', 'Security'],
                       ['Cloud Computing', 'System Admin', 'DevOps'],
                       ['Software Engineering', 'Database Management', 'Testing']]
        skills_hr = [['Recruitment', 'Training', 'Compensation'],
                     ['Employee Relations', 'Conflict Resolution', 'HR Policies'],
                     ['Talent Acquisition', 'Career Development', 'Compliance'],
                     ['Payroll', 'Benefits Management', 'Organizational Behavior']]
        positions_management = ['Team Lead', 'Operations Manager', 'Project Director']
        positions_tech = ['IT Analyst', 'Software Engineer', 'CTO']
        positions_hr = ['HR Assistant', 'HR Manager', 'HR Consultant', 'HR Director']
        
        new_workers = []

        for i in range(3):
            new_entry = manager.copy()
            new_entry['salary'] *= 1.1 * (i + 1)
            new_entry['age'] += 3 * i
            new_entry['skills'] = skills_management[i]
            new_entry['_id'] = str(ObjectId())
            new_entry['firstName'] = first_names[i]
            new_entry['lastName'] = last_names[i]
            new_entry['position'] = positions_management[i]
            new_entry['department'] = 'Management'
            new_workers.append(new_entry)

        for i in range(2):
            new_entry = manager.copy()
            new_entry['salary'] *= 1.23 * (i + 1)
            new_entry['age'] += 3 * i
            new_entry['skills'] = skills_tech[i]
            new_entry['_id'] = str(ObjectId())
            new_entry['firstName'] = first_names[i]
            new_entry['lastName'] = last_names[i]
            new_entry['position'] = positions_tech[i]
            new_entry['department'] = 'IT'
            new_workers.append(new_entry)

        for i in range(4):
            new_entry = manager.copy()
            new_entry['salary'] *= 1.14 * (i + 1)
            new_entry['age'] += 3 * i
            new_entry['skills'] = skills_hr[i]
            new_entry['_id'] = str(ObjectId())
            new_entry['firstName'] = first_names[i]
            new_entry['lastName'] = last_names[i]
            new_entry['position'] = positions_hr[i]
            new_entry['department'] = 'HR'
            new_workers.append(new_entry)

        collection.insert_many(new_workers)

# Реалізація підключення до SQLite
class SQLiteConnector(DBConnection):
    def connect(self):
        conn = sqlite3.connect("company.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age INTEGER,
                salary REAL,
                position TEXT,
                department TEXT
            )
        ''')
        conn.commit()
        return conn

    def fetch_manager(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees LIMIT 1")
        return cursor.fetchone()

    def fetch_workers(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        return cursor.fetchall()

    def duplicate_workers(self):
        conn = self.connect()
        cursor = conn.cursor()
        manager = self.fetch_manager()
        if manager:
            cursor.execute("""
                INSERT INTO employees (first_name, last_name, age, salary, position, department)
                VALUES (?, ?, ?, ?, ?, ?)
            """, ("New", "Employee", manager[3] + 3, manager[4] * 1.1, "Duplicated Position", "HR"))
        conn.commit()
        conn.close()
