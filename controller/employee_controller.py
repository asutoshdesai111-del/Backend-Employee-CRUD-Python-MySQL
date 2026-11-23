
from model.employeeModel import EmployeeModel


class EmployeeController:

    def __init__(self):
        self.model = EmployeeModel()

    # 1. ADD EMPLOYEE
    def add_employee(self, name, email, department, salary):
        return self.model.add_employee(
            name, email, department, salary
        )

    # 2. VIEW ALL EMPLOYEES
    def view_all_employees(self):
        return self.model.view_all_employees()

    # 3. SEARCH EMPLOYEE
    def search_employee(self, employee_id):
        return self.model.search_employee(employee_id)

    # 4. UPDATE EMPLOYEE
    def update_employee(self, employee_id, name, email, department, salary):
        return self.model.update_employee(
            employee_id, name, email, department, salary
        )

    # 5. DELETE EMPLOYEE
    def delete_employee(self, employee_id):
        return self.model.delete_employee(employee_id)

    # 6. CLOSE CONNECTION
    def close_connection(self):
        self.model.close_connection()
