# Day 029 - Traffic Data Validator

## 📚 Overview

Today, I learned and practiced **Exception Handling, Custom Exceptions, Modules, and Imports** in Python.

Instead of only learning the concepts theoretically, I built a small **Traffic Data Validator** that validates vehicle information and handles invalid inputs using custom exceptions.

This practical is inspired by real-world traffic management systems.

---

## 🎯 Learning Objectives

- Understand Exception Handling
- Learn `try` and `except`
- Understand `else` and `finally`
- Create Custom Exceptions
- Learn Modules and Imports
- Validate user input
- Handle invalid data safely

---

## 🚦 Practical: Traffic Data Validator

The program accepts three types of traffic data:

- Vehicle Number
- Vehicle Type
- Vehicle Speed

The entered data is validated before being accepted.

---

## ✅ Validation Rules

### 1. Vehicle Number

Vehicle number cannot be empty.

```text
❌ Empty vehicle number
✅ MH12AB1234