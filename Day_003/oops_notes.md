# Object-Oriented Programming (OOP) Notes

## 📖 Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects** and **classes**. It helps in writing reusable, organized, and maintainable code.

Python supports Object-Oriented Programming, making it easier to model real-world entities in software applications.

---

# 🏗️ Class

A **class** is a blueprint or template used to create objects. It defines the properties (attributes) and behaviors (methods) that objects will have.

### Example

```python
class Student:
    pass
```

---

# 👤 Object

An **object** is an instance of a class. Multiple objects can be created from the same class, each having its own data.

### Example

```python
student1 = Student()
student2 = Student()
```

---

# 🔨 Constructor

A **constructor** is a special method named `__init__()` that is automatically called when an object is created.

It is used to initialize object attributes.

### Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 🔑 self Keyword

`self` refers to the current object of the class.

It is used to access instance variables and methods inside the class.

### Example

```python
class Student:

    def __init__(self, name):
        self.name = name
```

---

# 📦 Instance Variables

Instance variables store data specific to each object.

### Example

```python
self.student_id
self.name
self.age
self.course
```

Each object has its own copy of these variables.

---

# ⚙️ Instance Methods

Instance methods define the behavior of an object.

### Example

```python
def display_student(self):
    print(self.name)
```

Methods can access and modify instance variables.

---

# 🌍 Real-World Example

Imagine a college management system.

### Class

Student

### Objects

- Rohan
- Amit
- Priya

Each student has different values for:

- Student ID
- Name
- Age
- Course

But all are created using the same `Student` class.

---

# ✅ Advantages of OOP

- Code Reusability
- Better Organization
- Easy Maintenance
- Improved Readability
- Real-world Modeling
- Scalability
- Easier Debugging

---

# 💻 Practical Project

Today's practical project:

**Student Management System**

Features implemented:

- Add Student
- Display Student
- Update Student

OOP concepts used:

- Class
- Object
- Constructor
- Instance Variables
- Instance Methods

---

# 🎯 Interview Questions

### 1. What is OOP?

Object-Oriented Programming is a programming paradigm that organizes code into classes and objects.

---

### 2. What is the difference between a Class and an Object?

| Class | Object |
|--------|--------|
| Blueprint | Instance of a class |
| Logical entity | Physical entity |
| Defines attributes and methods | Stores actual data |

---

### 3. What is a Constructor?

A constructor is a special method (`__init__`) that initializes object data automatically when an object is created.

---

### 4. What is the purpose of `self`?

`self` refers to the current object and allows access to its attributes and methods.

---

### 5. What are Instance Variables?

Instance variables belong to individual objects, and each object maintains its own values.

---

# 📝 Summary

Today I learned the fundamentals of Object-Oriented Programming in Python, including:

- Class
- Object
- Constructor
- `self` Keyword
- Instance Variables
- Instance Methods

I also applied these concepts by developing a **Student Management System**, strengthening my understanding of how OOP is used to organize and manage real-world applications.