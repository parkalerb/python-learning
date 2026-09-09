from functools import reduce


employees = [
    {"name": "Rohan", "department": "IT", "salary": 65000},
    {"name": "Amit", "department": "HR", "salary": 45000},
    {"name": "Sneha", "department": "Finance", "salary": 55000},
    {"name": "Priya", "department": "IT", "salary": 75000},
    {"name": "Rahul", "department": "Marketing", "salary": 40000}
]


# Filter employees with salary above 50000

high_salary_employees = list(
    filter(lambda employee: employee["salary"] > 50000, employees)
)

print("Employees with salary above 50000:")
for employee in high_salary_employees:
    print(employee)


# Increase salary by 10%

updated_salaries = list(
    map(lambda employee: employee["salary"] * 1.10, employees)
)

print("\nUpdated salaries:")
print(updated_salaries)


# Create a salary dictionary using dictionary comprehension

salary_data = {
    employee["name"]: employee["salary"]
    for employee in employees
}

print("\nEmployee salaries:")
print(salary_data)


# Find the highest salary using reduce()

highest_salary = reduce(
    lambda salary1, salary2: salary1 if salary1 > salary2 else salary2,
    updated_salaries
)

print("\nHighest updated salary:", highest_salary)


# Sort employees by salary

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

print("\nEmployees sorted by salary:")
for employee in sorted_employees:
    print(employee)


# List comprehension for employee names

employee_names = [
    employee["name"]
    for employee in employees
]

print("\nEmployee names:")
print(employee_names)