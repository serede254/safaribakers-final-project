

from models.departments import  (view_departments,add_department,create_department_table)
from models.helpers import (create_employee_table,exit_program,add_employee,delete_employee,view_employees,create_shift)

def main():
    create_employee_table()
    create_department_table()
    
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_employee()
        elif choice == "2":
            delete_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            create_shift()
        elif choice == "5":
            view_departments()
        elif choice == "6":
            department_name = input("Enter department name: ")
            add_department(department_name)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. View Employees")
    print("4. Create Shift")
    print("5. View Departments")
    print("6. Add Department")

if __name__ == "__main__":
    main()
