

import sqlite3

conn = sqlite3.connect('bakery.db')
c = conn.cursor()

def create_department_table():
    c.execute('''CREATE TABLE IF NOT EXISTS departments (
                    id INTEGER PRIMARY KEY,
                    name TEXT UNIQUE
                 )''')
    conn.commit()

def add_department(name):
    c.execute('''INSERT INTO departments (name) VALUES (?)''', (name,))
    conn.commit()
    print("Department added successfully.")

def view_departments():
    c.execute('''SELECT * FROM departments''')
    departments = c.fetchall()
    if not departments:
        print("No departments found.")
    else:
        print("Department ID | Name")
        for department in departments:
            print(*department)
