import sys

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, employee_id=None, salary=None):
        super().__init__(name, age)
        self.__employee_id = employee_id if employee_id is not None else "NOT_ASSIGNED"
        self.__salary = salary if salary is not None else 0.0

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative!")

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: ${float(self.__salary)}")

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


def main():
    people_list = []
    employees_list = []
    managers_list = []

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("Choose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            name = input("Enter Name: ")
            try:
                age = int(input("Enter Age: "))
                p = Person(name, age)
                people_list.append(p)
                print(f"\nPerson created with name: {name} and age: {age}.")
            except ValueError:
                print("Invalid input for age.")

        elif choice == '2':
            name = input("Enter Name: ")
            try:
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                
                emp = Employee(name, age, emp_id, salary)
                employees_list.append(emp)
                print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}")
            except ValueError:
                print("Invalid input data.")

        elif choice == '3':
            name = input("Enter Name: ")
            try:
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                dept = input("Enter Department: ")
                
                mgr = Manager(name, age, emp_id, salary, dept)
                managers_list.append(mgr)
                print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")
            except ValueError:
                print("Invalid input data.")

        elif choice == '4':
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            
            sub_choice = input("Enter your choice: ").strip()
            
            if sub_choice == '1':
                if not people_list:
                    print("No Person records found.")
                else:
                    print("\nPerson Details:")
                    for p in people_list:
                        p.display()
            elif sub_choice == '2':
                if not employees_list:
                    print("No Employee records found.")
                else:
                    print("\nEmployee Details:")
                    for emp in employees_list:
                        emp.display()
            elif sub_choice == '3':
                if not managers_list:
                    print("No Manager records found.")
                else:
                    print("\nManager Details:")
                    for mgr in managers_list:
                        mgr.display()
            else:
                print("Invalid option selected.")

        elif choice == '5':
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!")
            people_list.clear()
            employees_list.clear()
            managers_list.clear()
            sys.exit()

        else:
            print("Invalid choice. Please select from 1 to 5.")
            
        print("\n--- Choose another operation ---")

if __name__ == "__main__":
    main()