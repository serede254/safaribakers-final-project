

class Shift:
    def __init__(self, date, employee_id):
        self.date = date
        self.employee_id = employee_id

    def __repr__(self):
        return f"Shift(date='{self.date}', employee_id={self.employee_id})"
