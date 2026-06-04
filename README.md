# OOPs-principal-python
# Python OOP Tasks

This repository contains the implementation for Lab Assignment 5.5. The objective of this project is to apply core Object-Oriented Programming (OOP) principles—Abstraction, Encapsulation, Inheritance, and Polymorphism—using Python.

## Implementations Included

* **Shape Structures:** Created an abstract `Shape` base class to verify that directly instantiating it throws an error. It includes functional subclasses for `Rectangle` and `Circle` to calculate area and perimeter. I also included an `IncompleteShape` class to test how Python throws an error when a mandatory abstract method is omitted.
* **ML Model Interface:** Designed an `MLModel` abstract class to enforce a common interface. Subclasses `LinearRegressionModel` and `DecisionTreeModel` implement their own versions of `train()` and `predict()` to show polymorphism in action.
* **Bank Management System:** Built a banking simulation starting with a `BankAccount` class that uses private attributes (`__account_number` and `__balance`) to demonstrate encapsulation. Extended this into a `SavingsAccount` that calculates and applies interest, and a `CurrentAccount` that overrides withdrawals to allow transactions within an overdraft limit.

---

## How to Run

1. Open your terminal or command prompt.
2. Run the script directly using Python:

```bash
python main.py
