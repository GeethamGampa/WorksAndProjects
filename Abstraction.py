# ABSTRACTION : means hiding complex things and showing only what is needed.

## We use abstraction when:
# We want to hide internal logic and only show the interface (e.g., method names).
# We want to force child classes to follow a common structure.
# We are designing a base class for future use.

## How Do We Do It, in Python?
# Use from abc import ABC, abstractmethod
# Create a class that inherits from ABC (Abstract Base Class)
# Use @abstractmethod to define methods that must be implemented in child classes.

#====================================================================================#

# Create an abstract class Vehicle with an abstract method start_engine().
# Create child classes like Car and Bike that implement start_engine().

from abc import ABC, abstractmethod

class Vehicle(ABC):
  @abstractmethod
  def start_engine(self):
    pass

class Car(Vehicle):
    def start_engine(self):
      print("Car engine started")

class Bike(Vehicle):
    def start_engine(self):
      print("Bike engine started")

c = Car()
c.start_engine()

b = Bike()
b.start_engine()

#====================================================================================#

# Make an abstract class Shape with an abstract method area().
# Create classes like Circle, Rectangle, and Square that implement the area() method.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

c = Circle(2)
print("Area of Circle :", c.area())

r = Rectangle(4, 8)
print("Area of Rectangle:", r.area())

s = Square(4)
print("Area of Square:", s.area())

#====================================================================================#

# Define an abstract class Animal with make_sound() as an abstract method.
# Create Cat, Dog, and Cow classes to implement their own sounds.

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
        
class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")
        
class Dog(Animal):
    def make_sound(self):
        print("Woof!")
        
class Cow(Animal):
    def make_sound(self):
        print("Moo!")
        
d = Dog()
c = Cat()
w = Cow()

d.make_sound()
c.make_sound()
w.make_sound()

#====================================================================================#

# Create an abstract class Payment with abstract method pay(amount).
# Create two child classes: CreditCardPayment and PayPalPayment, 
# each with their own pay() logic.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")
    
class PaypalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Paypal")    
        
        
c = CreditCardPayment()
p = PaypalPayment()

c.pay(1000)
p.pay(500)

#====================================================================================#

# Make an abstract class Notification with a method send(message).
# Create classes like EmailNotification and SMSNotification that implement 
# how messages are sent.

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")
        
class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")
        
e = EmailNotification()
s = SMSNotification()

e.send("Hello Ammu via Email")
s.send("Hi via SMS")
        
#====================================================================================#

# Define an abstract class Employee with method calculate_salary().
# Create classes FullTimeEmployee and PartTimeEmployee with 
# different salary calculation logic.

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.salary = monthly_salary

    def calculate_salary(self):
        return self.salary

class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate

f = FullTimeEmployee(45000)
print("Full-time salary:", f.calculate_salary())

p = PartTimeEmployee(80, 100)
print("Part-time salary:", p.calculate_salary())

#====================================================================================#

# DECORATORS : a special function that adds extra features to another function 
# without changing the original function's code.

## Example :

def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# Where do we use Decorators?

# Logging: Keep track of when functions are used.
# Authorization: Allow access only if the user is logged in.
# Measuring time: See how long a function takes.
# Code reuse: Add common behavior to many functions

#====================================================================================#

# Custom Decorator — Logging Function Calls

from datetime import datetime

def log(func):
    def wrapper():
        print(f"[LOG] {func.__name__} called at {datetime.now()}")
        func()
    return wrapper

@log
def greet():
    print("Hello, Geetham!")

greet()

#====================================================================================#

# @staticmethod — Utility Function That Doesn’t Use self

class Math:
    @staticmethod
    def square(n):
        return n * n

print("Square of 5 is:", Math.square(5))  


# @staticmethod to Check if a Number is Even

class NumberCheck:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

print("Is 10 even?", NumberCheck.is_even(8))   
print("Is 7 even?", NumberCheck.is_even(3)) 

#====================================================================================#

# @classmethod — Changing a Class Variable

class University:
    school_name = "Old University"

    @classmethod
    def change_name(cls, new_name):
        cls.university_name = new_name

print(University.school_name)
University.change_name("EKU University")
print(University.university_name)

#====================================================================================#

# @check_positive Decorator — Prevent Negative Inputs

def check_positive(func):
    def wrapper(a, b):
        if a < 0 or b < 0:
            return "Both numbers must be positive!"
        return func(a, b)
    return wrapper

@check_positive
def diff(a, b):
    return a - b

print(diff(10, 3))    
print(diff(-5, 3))    

#====================================================================================#

#  @repeat Decorator — Repeat a Function N Times

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Run {i+1}: {func(*args, **kwargs)}")
        return wrapper
    return decorator

@repeat(3) # repeats 3 times
def greet(name):
    return f"Hello, {name}!"

greet("Geetham")

#====================================================================================#

# Research Topic

from abc import ABC, abstractmethod

class Animal(ABC):
   @abstractmethod
   def make_sound(self):
       print("make a sound")
       pass

   def make_s(self):
      return("make a sound in make_s")

class Dog(Animal):
  def make_sound(self):
    return "Bark"

d = Dog()
print(d.make_sound())
print(d.make_s())

A = Animal()
print(A.make_s())


# Why does A = Animal() give an error?

# Animal is an abstract class because it uses ABC and @abstractmethod.
# The method make_sound() is abstract, which means
# any class that inherits from Animal must write its own version of make_sound().
# Because of that, Python does NOT allow creating an object of Animal directly.

# To fix this:
# Option 1: Remove @abstractmethod if you want to use Animal directly
# Option 2: Create a child class that provides its own version of make_sound()

# This line gives error if used directly
# A = Animal()  

# Correct way using a child class:
class A_Animal(Animal):
    def make_sound(self):
        return "No sound"

A = A_Animal()
print(A.make_s()) 













