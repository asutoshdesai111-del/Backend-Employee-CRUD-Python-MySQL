
from controller.employee_controller import EmployeeController


def main():

    controller = EmployeeController()

    try:
        while True:

            print("\n================================")
            print("   EMPLOYEE MANAGEMENT SYSTEM")
            print("================================")
            print("1. Add Employee")
            print("2. View All Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")
            print("================================")

            choice = input("Enter your choice: ")

            # ADD EMPLOYEE
            if choice == '1':

                print("\n--- Add Employee ---")

                name = input("Enter Name: ")
                email = input("Enter Email: ")
                department = input("Enter Department: ")
                salary = float(input("Enter Salary: "))

                controller.add_employee(
                    name, email, department, salary
                )

                print("Employee added successfully!")

            # VIEW ALL EMPLOYEES
            elif choice == '2':

                print("\n--- ALL EMPLOYEE DETAILS ---")

                employees = controller.view_all_employees()

                if employees:

                    headers = [
                        "Employee ID",
                        "Name",
                        "Email",
                        "Department",
                        "Salary"
                    ]

                    rows = [headers] + [
                        [str(value) for value in employee]
                        for employee in employees
                    ]
                    widths = [
                        max(len(row[index]) for row in rows)
                        for index in range(len(headers))
                    ]
                    separator = "+" + "+".join(
                        "-" * (width + 2) for width in widths
                    ) + "+"

                    print(separator)
                    for row_index, row in enumerate(rows):
                        print("| " + " | ".join(
                            value.ljust(width)
                            for value, width in zip(row, widths)
                        ) + " |")
                        if row_index == 0:
                            print(separator)
                    print(separator)

                else:
                    print("No employee records found!")

            # SEARCH EMPLOYEE
            elif choice == '3':

                print("\n--- Search Employee ---")

                employee_id = int(input("Enter Employee ID: "))

                employee = controller.search_employee(employee_id)

                if employee:
                    print("Employee Found!")
                    print("ID         :", employee[0])
                    print("Name       :", employee[1])
                    print("Email      :", employee[2])
                    print("Department :", employee[3])
                    print("Salary     :", employee[4])
                else:
                    print("Employee not found!")

            # UPDATE EMPLOYEE
            elif choice == '4':

                print("\n--- Update Employee ---")

                employee_id = int(input("Enter Employee ID: "))

                employee = controller.search_employee(employee_id)

                if employee:

                    name = input("Enter New Name: ")
                    email = input("Enter New Email: ")
                    department = input("Enter New Department: ")
                    salary = float(input("Enter New Salary: "))

                    result = controller.update_employee(
                        employee_id,
                        name,
                        email,
                        department,
                        salary
                    )

                    if result:
                        print("Employee updated successfully!")
                    else:
                        print("No changes made!")

                else:
                    print("Employee not found!")

            # DELETE EMPLOYEE
            elif choice == '5':

                print("\n--- Delete Employee ---")

                employee_id = int(input("Enter Employee ID: "))

                employee = controller.search_employee(employee_id)

                if employee:

                    print("Employee Name:", employee[1])

                    confirm = input(
                        "Are you sure you want to delete? (yes/no): "
                    )

                    if confirm.lower() == 'yes':

                        result = controller.delete_employee(employee_id)

                        if result:
                            print("Employee deleted successfully!")
                        else:
                            print("Unable to delete employee!")

                    else:
                        print("Delete cancelled!")

                else:
                    print("Employee not found!")

            # EXIT
            elif choice == '6':

                print("\nThank you for using Employee Management System!")
                break

            else:
                print("Invalid choice! Please select 1 to 6.")

    except Exception as e:
        print("Something went wrong:", e)

    finally:
        controller.close_connection()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
