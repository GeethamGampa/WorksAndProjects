## ENCAPSULATION

# Create a class Person with a public variable name and a 
# private variable age. Write methods to get and set the age (encapsulation).

class Person:
    def __init__(self, name, age):
        self.name = name  # Public variable
        self.__age = age  # Private variable

    def set_age(self, age):
        if age > 0:
            self.__age = age

    def get_age(self):
        return self.__age

person = Person("Geetham", 25)
print(person.name)  # Access public variable
print(person.get_age())  # Access private variable using method

person.set_age(30)
print(person.get_age())  # Access updated private variable using method

#==============================================================================#

# Create a class Employee with a protected variable salary. 
# Derive a class Manager from Employee and access the protected variable salary in Manager.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary # Protected variable
        
class Manager(Employee):
    def display_salary(self):
        print(f"Manager's Salary: {self._salary}")
        
emp = Manager("Emmy", 50000)
emp.display_salary()

#==============================================================================#

# Create a class BankAccount with a private variable balance. 
# Write methods to deposit and withdraw money while ensuring that the balance cannot go below 0.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")
            
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Funds")
    
    def get_balance(self):
        return self.__balance
    

account = BankAccount("Geetham", 1000)
account.deposit(500)
print(account.get_balance()) 

#==============================================================================#

# Create a class Car with a public variable make, a protected variable _model, 
# and a private variable __price. Write methods to get and set the price, 
# and display all the attributes.

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self._model = model
        self.__price = price
        
    def set_price(self, price):
        if price > 0:
            self.__price = price
    
    def get_price(self):
        return self.__price
    
    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self._model}")
        print(f"Car Price: {self.get_price()}")
        
car = Car("Audi", "A3", 50000)
car.display_info()

car.set_price(45000)
car.display_info()

#==============================================================================#

# Create a class Vehicle with public, private, and protected variables. 
# Create a derived class and demonstrate how encapsulation works 
# when accessing these variables.

class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand  # Public variable
        self._model = model  # Protected variable
        self.__price = price  # Private variable

    def set_price(self, price):
        if price > 0:
            self.__price = price

    def get_price(self):
        return self.__price

class Car(Vehicle):
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self._model}")
        print(f"Price: {self.get_price()}")  

car = Car("MorrisGarages", "Gloster", 75000)
car.display_details()  

car.set_price(70000)   
car.display_details()   

#==============================================================================#

# Create a class Rectangle with private attributes for width and height. 
# Use getters and setters to set and retrieve the dimensions, 
# and calculate the area using a property.

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # Getter for width
    def get_width(self):
        return self.__width

    # Setter for width
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Width must be positive.")

    # Getter for height
    def get_height(self):
        return self.__height

    # Setter for height
    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("Height must be positive.")

    # Property for area
    @property
    def area(self):
        return self.__width * self.__height
 
rect = Rectangle(5, 10)
print(f"Width: {rect.get_width()}, Height: {rect.get_height()}")
print(f"Area: {rect.area}") 

rect.set_width(6)
rect.set_height(12)
print(f"New Area: {rect.area}")  

#==============================================================================#

# Create a class Employee with private attributes for name and salary. 
# Use getters and setters for these attributes, and use a 
# property to calculate the annual salary (salary * 12)


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")

    # Property for annual salary
    @property
    def annual_salary(self):
        return self.__salary * 12


emp = Employee("Hash", 5000)
print(f"Employee: {emp.get_name()}, Monthly Salary: {emp.get_salary()}")
# Access annual salary using property
print(f"Annual Salary: {emp.annual_salary}") 

emp.set_salary(6000)
print(f"Updated Annual Salary: {emp.annual_salary}")

