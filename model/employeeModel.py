
from config.db import get_connection


class EmployeeModel:

    def __init__(self):

        self.conn = get_connection()

        self.cursor = self.conn.cursor()

    # 1. ADD EMPLOYEE
    def add_employee(self, name, email, department, salary):

        query = """
        INSERT INTO employees (name, email, department, salary)
        VALUES (%s, %s, %s, %s)
        """

        self.cursor.execute(
            query, (name, email, department, salary)
        )

        self.conn.commit()

    # 2. VIEW ALL EMPLOYEES
    def view_all_employees(self):

        query = "SELECT * FROM employees"

        self.cursor.execute(query)

        return self.cursor.fetchall()

    # 3. SEARCH EMPLOYEE
    def search_employee(self, employee_id):

        query = "SELECT * FROM employees WHERE employee_id = %s"

        self.cursor.execute(query, (employee_id,))

        return self.cursor.fetchone()

    # 4. UPDATE EMPLOYEE
    def update_employee(self, employee_id, name, email, department, salary):

        query = """
        UPDATE employees
        SET name = %s,
            email = %s,
            department = %s,
            salary = %s
        WHERE employee_id = %s
        """

        self.cursor.execute(
            query,
            (name, email, department, salary, employee_id)
        )

        self.conn.commit()

        return self.cursor.rowcount > 0

    # 5. DELETE EMPLOYEE
    def delete_employee(self, employee_id):

        query = "DELETE FROM employees WHERE employee_id = %s"

        self.cursor.execute(query, (employee_id,))

        self.conn.commit()

        return self.cursor.rowcount > 0

    # 6. CLOSE CONNECTION
    def close_connection(self):

        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()
