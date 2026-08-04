# Day 022 - Employee Management System using OOP & File Handling

## 📚 Overview

Welcome to **Day 022** of my Python learning journey.

Today, I explored advanced Object-Oriented Programming (OOP) concepts along with File Handling by building an **Employee Management System**.

This project demonstrates how to organize code using classes, implement inheritance and polymorphism, and store employee records permanently using text files.

---

# 🎯 Learning Objectives

- Understand Inheritance
- Learn Polymorphism
- Understand Encapsulation
- Learn File Handling
- Read and Write Files
- Use `with open()`
- Build a real-world console application

---

# 📂 Folder Structure

```text
Day_004/
│
├── employee_management.py
├── employees.txt
├── oop_file_notes.md
└── README.md
```

---

# 📖 Topics Covered

- Object-Oriented Programming (OOP)
- Inheritance
- Polymorphism
- Encapsulation
- File Handling
- File Modes
- Exception Handling
- `with open()`

---

# 💻 Practical Project

## Employee Management System

The project is a menu-driven console application that allows users to manage employee records using Object-Oriented Programming and File Handling.

---

# ✨ Features

### ✅ Add Employee

Add a new employee by entering:

- Employee ID
- Employee Name
- Department
- Salary

Employee information is automatically stored in **employees.txt**.

---

### ✅ View Employees

Displays all employee records stored in the file.

---

### ✅ Search Employee

Search an employee using the Employee ID.

---

### ✅ Persistent Storage

Employee data remains saved even after the program is closed because records are stored in a text file.

---

# 🏗️ OOP Concepts Used

## Inheritance

The `Employee` class inherits common properties from the `Person` class.

---

## Polymorphism

The `display()` method is overridden in the `Employee` class to display employee-specific information.

---

## Encapsulation

Employee data is protected inside the class using attributes and methods.

---

# 📂 File Handling Concepts

The project uses Python File Handling to:

- Create files
- Read employee data
- Write employee data
- Append new records

Example:

```python
with open("employees.txt", "a") as file:
    file.write(data)
```

---

# 📈 Skills Gained

After completing today's project, I learned how to:

- Design reusable classes
- Apply inheritance in Python
- Override methods using polymorphism
- Protect object data through encapsulation
- Store application data in files
- Read and search file contents
- Build a practical console-based application

---

# 🧠 Key Takeaways

- OOP makes code modular, reusable, and easier to maintain.
- Inheritance reduces duplicate code.
- Polymorphism allows the same method to behave differently.
- Encapsulation helps protect object data.
- File Handling enables persistent storage without using a database.
- `with open()` is the recommended way to work with files because it automatically closes the file after use.

---

# 📊 Progress

| Topic | Status |
|--------|--------|
| Inheritance | ✅ Completed |
| Polymorphism | ✅ Completed |
| Encapsulation | ✅ Completed |
| File Handling | ✅ Completed |
| Read File | ✅ Completed |
| Write File | ✅ Completed |
| Search Employee | ✅ Completed |
| Employee Management System | ✅ Completed |

---

# 🚀 Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub

---

# 🎤 Interview Preparation

Topics covered today:

- Four Pillars of OOP
- Inheritance
- Polymorphism
- Encapsulation
- File Handling
- File Modes (`r`, `w`, `a`)
- Why use `with open()`
- Exception Handling (`FileNotFoundError`)

---

# 📌 What's Next?

In the next learning session, I will continue exploring advanced Python concepts and build more practical applications using Exception Handling and Modules.

---

# 👨‍💻 Author

**Rohan Parkale**

- MCA Student
- Python Developer
- AIML Enthusiast
- Passionate about Software Development, Machine Learning, and Problem Solving

---

⭐ Thank you for visiting this repository! Feel free to explore my other learning repositories and follow my Python learning journey on GitHub.