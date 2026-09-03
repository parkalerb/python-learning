# Day 036 - Python Advanced Concepts

## Overview

Practiced advanced Python concepts that are useful for backend and Django development.

## Topics Covered

- Decorators
- *args
- **kwargs
- Generators
- yield
- Iterators vs Generators

## Practical Programs

### 1. Logging Decorator

Created a simple logging decorator that prints information whenever a function is called.

It also demonstrates how `*args` and `**kwargs` can be used inside a decorator.

### 2. Traffic Data Generator

Created a generator function to return traffic records one at a time using `yield`.

This approach is useful when working with large amounts of data because records can be processed one by one.

## Key Learning

### Decorator

A decorator is a function that adds extra functionality to another function without changing its original code.

### *args

`*args` is used to handle multiple positional arguments.

### **kwargs

`**kwargs` is used to handle multiple keyword arguments.

### yield

`yield` is used in generator functions to return values one at a time.

### Generator

A generator produces values one by one instead of storing all values in memory at once.

## Interview Focus

- What is a decorator?
- What is the difference between `yield` and `return`?
- Why are generators memory efficient?
- What is the difference between `*args` and `**kwargs`?
- What is the difference between an iterator and a generator?

## Files

- `decorators.py` - Logging decorator and function arguments
- `generators.py` - Traffic data generator using `yield`