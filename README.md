# Employee Management System

## Project Overview
This project is a console-based Employee Management System built in Python. The main objective is to implement core Object-Oriented Programming (OOP) concepts such as Classes, Inheritance, Encapsulation, Method Overriding, and Polymorphism. 

The system allows creating and managing records for different roles: general Persons, Employees, and Managers, while maintaining a clean, user-friendly interactive menu.

---

## OOP Concepts Implemented

* **Classes & Objects**: Created base classes (`Person`, `Employee`) and specialized derived classes (`Manager`, `Developer`).
* **Inheritance**: Derived classes inherit core properties like `name` and `age` from the parent `Person` class using the `super()` function.
* **Encapsulation**: Sensitive attributes such as `__employee_id` and `__salary` are kept private (using double underscores) and are only accessible through proper Getter and Setter methods.
* **Method Overriding**: The `display()` method has been overridden in the child classes to print specific details tailored to that role (e.g., Department for Managers).
* **Constructor & Destructor**: Implemented `__init__` constructors to initialize object attributes and a basic structure for resource management/cleanup.

---

## Design Assumptions & Decisions
1. **Pythonic Method Overloading**: Since Python does not support traditional method overloading by default, we implemented it cleanly using default arguments (`None`) in the constructor to allow flexible object creation.
2. **Explicit Memory Management**: In the exit choice (`Option 5`), lists are explicitly cleared to demonstrate proper cleanup and triggering of destruction principles before the application quits.

---

## How to Run the Project
1. Make sure you have Python installed on your system.
2. Open your terminal or command prompt in the project directory.
3. Run the following command:
   ```bash
   python main.py
