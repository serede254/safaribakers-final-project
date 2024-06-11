import sys

def exit_program():
    print("Exiting the program.")
    sys.exit(0)

import sqlite3

conn = sqlite3.connect('bakery.db')
c = conn.cursor()

def create_employee_table():
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    position TEXT,
                    salary REAL,
                    department_name TEXT,
                    FOREIGN KEY (department_name) REFERENCES departments(name)
                 )''')
    conn.commit()

def add_employee():
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))
    department_name = input("Enter department name: ")
    c.execute('''INSERT INTO employees (name, position, salary, department_name)
                 VALUES (?, ?, ?, ?)''', (name, position, salary, department_name))
    conn.commit()
    print("Employee added successfully.")

def delete_employee():
    employee_id = int(input("Enter employee ID to delete: "))
    c.execute('''DELETE FROM employees WHERE id = ?''', (employee_id,))
    conn.commit()
    print("Employee deleted successfully.")

def view_employees():
    c.execute('''SELECT * FROM employees''')
    employees = c.fetchall()
    if not employees:
        print("No employees found.")
    else:
        print("Employee ID | Name | Position | Salary | Department Name")
        for employee in employees:
            print(*employee)

def create_shift():
    date = input("Enter shift date (YYYY-MM-DD): ")
    employee_id = int(input("Enter employee ID: "))
    c.execute('''INSERT INTO shifts (date, employee_id)
                 VALUES (?, ?)''', (date, employee_id))
    conn.commit()
    print("Shift created successfully.")
