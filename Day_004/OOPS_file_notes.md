# OOP & File Handling Notes

## 📖 Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **classes** and **objects**. It helps developers write reusable, modular, and maintainable software.

File Handling allows a program to store and retrieve data from files, making the data persistent even after the program terminates.

Today's project combines OOP concepts with File Handling to build a simple **Employee Management System**.

---

# 🏛️ Four Pillars of OOP

The four fundamental principles of Object-Oriented Programming are:

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

# 🔒 Encapsulation

Encapsulation is the process of wrapping data and methods into a single unit (class) while restricting direct access to the data.

It protects data from accidental modification.

### Example

```python
class Employee:

    def __init__(self, name):
        self._name = name
```

The underscore (`_`) indicates that the variable is intended for internal use.

---

# 👨‍👦 Inheritance

Inheritance allows one class to acquire the properties and methods of another class.

It promotes code reusability.

### Example

```python
class Person:

    def __init__(self, name):
        self.name = name


class Employee(Person):

    def __init__(self, name):
        super().__init__(name)
```

Here:

- Person → Parent Class
- Employee → Child Class

---

# 🔄 Polymorphism

Polymorphism means "many forms."

A child class can redefine a method inherited from the parent class.

### Example

```python
class Person:

    def display(self):
        print("Person")


class Employee(Person):

    def display(self):
        print("Employee")
```

The `display()` method behaves differently depending on the object.

---

# 📂 File Handling

File handling allows Python programs to:

- Create files
- Read files
- Write files
- Append data
- Store information permanently

---

# 📄 Opening a File

Syntax

```python
file = open("employees.txt", "r")
```

However, this approach requires manually closing the file.

---

# ✅ Using with open()

Recommended syntax

```python
with open("employees.txt", "r") as file:
    data = file.read()
```

Advantages

- Automatically closes the file
- Cleaner code
- Prevents resource leaks
- Handles exceptions more safely

---

# 📌 File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read file |
| `"w"` | Write file (overwrites existing content) |
| `"a"` | Append data to the end of the file |
| `"x"` | Create a new file |
| `"r+"` | Read and write |

---

# 📖 Reading a File

```python
with open("employees.txt", "r") as file:
    data = file.read()
```

---

# ✍️ Writing to a File

```python
with open("employees.txt", "w") as file:
    file.write("Hello")
```

---

# ➕ Appending Data

```python
with open("employees.txt", "a") as file:
    file.write("New Employee\n")
```

---

# 🌍 Real-World Applications

File Handling is used in:

- Student Management Systems
- Employee Management Systems
- Banking Applications
- Inventory Systems
- Attendance Systems
- Log Files
- Configuration Files
- Data Storage

---

# 💻 Practical Project

Today's Project:

**Employee Management System**

### Features

- Add Employee
- Save Employee to File
- View Employees
- Search Employee

---

# 🎯 Interview Questions

## 1. What is OOP?

Object-Oriented Programming is a programming paradigm based on classes and objects.

---

## 2. What are the four pillars of OOP?

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

## 3. What is Inheritance?

Inheritance allows one class to inherit the properties and methods of another class.

---

## 4. What is Polymorphism?

Polymorphism allows the same method to behave differently depending on the object.

---

## 5. What is Encapsulation?

Encapsulation protects data by restricting direct access and combining data with methods inside a class.

---

## 6. Why do we use `with open()`?

Because it:

- Automatically closes the file
- Prevents memory leaks
- Produces cleaner and safer code

---

## 7. Difference between `"w"` and `"a"` mode?

| `"w"` | `"a"` |
|--------|--------|
| Overwrites the file | Adds new data at the end |
| Existing content is removed | Existing content remains |

---

## 8. Difference between Text File and Binary File?

| Text File | Binary File |
|------------|-------------|
| Stores readable characters | Stores binary data |
| Uses `.txt` | Uses formats like `.jpg`, `.png`, `.exe` |

---

# 📝 Summary

Today I learned advanced Object-Oriented Programming concepts and combined them with File Handling to build an **Employee Management System**.

### Key Concepts Covered

- Encapsulation
- Inheritance
- Polymorphism
- File Handling
- File Modes
- `with open()`

The project demonstrated how object-oriented design and file operations can be used together to build maintainable and practical applications.