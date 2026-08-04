"""
Employee Management System

Author: Rohan Parkale
Day 022 - Python OOP + File Handling

Concepts Used:
- Class
- Object
- Inheritance
- Polymorphism
- Encapsulation
- File Handling
"""

FILE_NAME = "employees.txt"


class Person:
    """Base class representing a person."""

    def __init__(self, name: str):
        self._name = name

    def display(self):
        """Display person details."""
        print(f"Name : {self._name}")


class Employee(Person):
    """Employee class derived from Person."""

    def __init__(
        self,
        employee_id: int,
        name: str,
        department: str,
        salary: float
    ):
        super().__init__(name)

        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display(self):
        """Display employee details (Polymorphism)."""

        print("\nEmployee Details")
        print("-" * 35)
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self._name}")
        print(f"Department  : {self.department}")
        print(f"Salary      : ₹{self.salary:.2f}")

    def to_file(self):
        """Convert employee object into text."""

        return (
            f"{self.employee_id},"
            f"{self._name},"
            f"{self.department},"
            f"{self.salary}\n"
        )


class EmployeeManager:
    """Manage employee operations."""

    def add_employee(self):
        """Add a new employee."""

        print("\nAdd Employee")

        employee_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(
            employee_id,
            name,
            department,
            salary
        )

        with open(FILE_NAME, "a") as file:
            file.write(employee.to_file())

        print("\nEmployee saved successfully.")

    def view_employees(self):
        """Display all employees."""

        try:

            with open(FILE_NAME, "r") as file:

                lines = file.readlines()

                if not lines:
                    print("\nNo employee records found.")
                    return

                print("\n========== Employee List ==========")

                for line in lines:

                    employee_id, name, department, salary = (
                        line.strip().split(",")
                    )

                    employee = Employee(
                        int(employee_id),
                        name,
                        department,
                        float(salary)
                    )

                    employee.display()

        except FileNotFoundError:
            print("\nEmployee file does not exist.")

    def search_employee(self):
        """Search employee by ID."""

        try:

            search_id = input("\nEnter Employee ID: ")

            with open(FILE_NAME, "r") as file:

                found = False

                for line in file:

                    employee_id, name, department, salary = (
                        line.strip().split(",")
                    )

                    if employee_id == search_id:

                        employee = Employee(
                            int(employee_id),
                            name,
                            department,
                            float(salary)
                        )

                        employee.display()

                        found = True
                        break

                if not found:
                    print("\nEmployee not found.")

        except FileNotFoundError:
            print("\nEmployee file does not exist.")


def main():
    """Main Function."""

    manager = EmployeeManager()

    while True:

        print("\n========== Employee Management ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.add_employee()

        elif choice == "2":
            manager.view_employees()

        elif choice == "3":
            manager.search_employee()

        elif choice == "4":
            print("\nThank you for using Employee Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()