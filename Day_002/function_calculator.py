"""
Project: Function Based Calculator
Author: Rohan Parkale

Description:
A simple menu-driven calculator using Python functions.
"""

def add(a: float, b: float) -> float:
    """Returns the addition of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Returns the subtraction of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns the multiplication of two numbers."""
    return a * b


def divide(a: float, b: float):
    """Returns the division of two numbers."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def display_menu():
    """Displays calculator menu."""
    print("\n========== Function Based Calculator ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    """Main function to run the calculator."""

    while True:

        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid Choice! Try Again.")
            continue

        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))


if __name__ == "__main__":
    main()