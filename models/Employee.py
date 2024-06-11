

class Employee:
    def __init__(self, name, position, salary, department_name):
        self.name = name
        self.position = position
        self.salary = salary
        self.department_name = department_name

    def __repr__(self):
        return f"Employee(name='{self.name}', position='{self.position}', salary={self.salary}, department_name='{self.department_name}')"
