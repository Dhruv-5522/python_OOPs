from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class IncompleteShape(Shape):
    def area(self):
        return 10


class MLModel(ABC):
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass

class LinearRegressionModel(MLModel):
    def train(self):
        print("Linear Regression Training")
        
    def predict(self):
        print("Linear Regression Prediction")

class DecisionTreeModel(MLModel):
    def train(self):
        print("Decision Tree Training")
        
    def predict(self):
        print("Decision Tree Prediction")


class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass
        
    @abstractmethod
    def withdraw(self, amount):
        pass

class BankAccount(Account):
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    def set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount} | Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount} | Balance: {self.__balance}")
            return True
        else:
            print("Insufficient balance")
            return False

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        self.deposit(interest)

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if amount <= (self.get_balance() + self.overdraft_limit):
            new_balance = self.get_balance() - amount
            self.set_balance(new_balance)
            print(f"Withdrawn with overdraft: {amount} | Balance: {self.get_balance()}")
            return True
        else:
            print("Overdraft limit exceeded")
            return False


if __name__ == "__main__":
    try:
        s = Shape()
    except TypeError as e:
        print(f"Error: {e}")

    try:
        bad_shape = IncompleteShape()
    except TypeError as e:
        print(f"Error: {e}")

    r = Rectangle(10, 5)
    print(f"Rectangle Area: {r.area()} | Perimeter: {r.perimeter()}")
    
    c = Circle(7)
    print(f"Circle Area: {round(c.area(), 2)} | Perimeter: {round(c.perimeter(), 2)}")

    models = [LinearRegressionModel(), DecisionTreeModel()]
    for model in models:
        model.train()
        model.predict()

    sav = SavingsAccount("SAV999", 4000, 3.5)
    sav.deposit(1000)
    sav.add_interest()
    sav.withdraw(1500)
    
    curr = CurrentAccount("CUR111", 1500, 500)
    curr.deposit(500)
    curr.withdraw(2300)