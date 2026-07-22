"""
Student Management System

Author: Rohan Parkale
Day 003 - Object-Oriented Programming (OOP)

Concepts Used:
- Class
- Object
- Constructor
- Instance Variables
- Instance Methods
"""


class Student:
    """Represents a student."""

    def __init__(self, student_id: int, name: str, age: int, course: str):
        """Initialize student details."""
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_student(self):
        """Display student details."""
        print("\nStudent Details")
        print("-" * 30)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")

    def update_student(self, name: str, age: int, course: str):
        """Update student details."""
        self.name = name
        self.age = age
        self.course = course
        print("\nStudent details updated successfully.")


students = []


def add_student():
    """Add a new student."""

    print("\nAdd Student")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    student = Student(student_id, name, age, course)
    students.append(student)

    print("\nStudent added successfully.")


def display_students():
    """Display all students."""

    if not students:
        print("\nNo student records found.")
        return

    print("\n===== Student List =====")

    for student in students:
        student.display_student()


def update_student():
    """Update an existing student."""

    if not students:
        print("\nNo student records found.")
        return

    student_id = int(input("\nEnter Student ID to update: "))

    for student in students:
        if student.student_id == student_id:

            print("\nEnter New Details")

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")

            student.update_student(name, age, course)
            return

    print("\nStudent not found.")


def main():
    """Main function."""

    while True:

        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()