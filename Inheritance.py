## SINGLE INHERITANCE : One child class inherits from one parent class

# **QUESTION-1**
# Create a class Device with a method show_type() that prints "This is a generic device."
# Create a class Mobile that inherits from Device and call the show_type() method using a Mobile object.

class Device:
    def show_type(self):
        print("QUESTION 1 : This is a generic device")
        
class Mobile(Device):
    pass

m = Mobile()
m.show_type()

# **QUESTION-2**
# Now modify the Mobile class to override the show_type() method and print "This is a mobile device."
# Call the method and observe the output.

class Device:
    def show_type(self):
        print("QUESTION 1 : This is a generic device.")

class Mobile(Device):
    def show_type(self):
        print("QUESTION 2 : This is a mobile device.")

m = Mobile()
m.show_type()

#===================================================================================#

## MULTIPLE INHERITANCE : One child class inherits from more than one parent class.

# **QUESTION-3**
# Create two classes:
# Mother with method skills() that prints "Cooks well"
# Father with method skills() that prints "Drives well"
# Then create a Child class that inherits from both and call skills().

class Mother():
    def skills(self):
        print("QUESTION 3 : Cooks well")
        
class Father():
    def skills(self):
        print("Drives well")
        
class Child(Mother, Father):
    pass

c = Child()
c.skills()


# **QUESTION-4**
# Override in Child to Use Both Parent Methods

class Mother:
    def skills(self):
        print("QUESTION 4 : Cooks well")

class Father:
    def skills(self):
        print("Drives well")

class Child(Mother, Father):
    def skills(self):
        Mother.skills(self)
        Father.skills(self)

c = Child()
c.skills()

#===================================================================================#

## MULTILEVEL INHERITANCE : A class inherits from a child class which already inherited from another class

# **QUESTION-5**
# Create three classes:
# Grandparent with method show(): prints "I am Grandparent"
# Parent inherits Grandparent
# Child inherits Parent
# Create an object of Child and call show().

class Grandparent():
    def show(self):
        print("QUESTION 5 : I am Grandparent")
        
class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.show()

#===================================================================================#

## HIERARCHICAL INHERITANCE : Multiple child classes inherit from the same parent class.

# **QUESTION-6**
# Create a class Vehicle with method start(): prints "Vehicle started".
# Create two child classes: Car and Bike, both inheriting from Vehicle.
# Call start() from objects of both Car and Bike.

class Vehicle:
    def start(self):
        print("QUESTION 6 : Vehicle started")
        
class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = Car()
b = Bike()

c.start()
b.start()

#===================================================================================#

## HYBRID INHERITANCE : Combination of two or more types of inheritance (like multiple + multilevel).

# **QUESTION-7**
# Create the following class structure:
# ClassA has method method_A()
# ClassB and ClassC inherit from ClassA
# ClassD inherits from both ClassB and ClassC
# Call method_A() using an object of ClassD.
    

class ClassA:
    def method_A(self):
        print("QUESTION 7 : This is method A from ClassA")

class ClassB(ClassA):
    pass

class ClassC(ClassA):
    pass

class ClassD(ClassB, ClassC):
    pass

d = ClassD()
d.method_A()

#===================================================================================#

## POLYMORPHISM : Same function name works in different ways for different classes.

# **QUESTION-8**
# METHOD OVERRIDING

# Create a base class Shape with method area() that prints "Area not defined".
# Create two child classes: Rectangle and Circle, and override area() in both.
# Create objects and call area()

class Shape():
    def area(self):
        print("QUESTION 8 : Area not defined")
        
class Rectangle(Shape):
    def area(self):
        print("QUESTION 8(a) : Area of Rectangle not defined")
        
class Circle(Shape):
    def area(self):
        print("QUESTION 8(b) : Area of Circle not defined")
        
s = Shape()
r = Rectangle()
c = Circle()

s.area()
r.area()
c.area()

#===================================================================================#

# **QUESTION-9**
# DUCK TYPING

# Create two classes: Writer and Painter.
# Both should have a method work()
# Writer.work() should print "Writing an article..."
# Painter.work() should print "Painting a picture..."
# Then create a function do_work(person) that calls person.work().
# Pass both Writer and Painter objects to this function and observe polymorphism.

class Writer():
    def work(self):
        print("QUESTION 9 : Writing an article")


class Painter():
    def work(self):
        print("QUESTION 9(a) : Painting a picture")
        

def do_work(Person):
    Person.work()
    
writer = Writer()
painter = Painter()

do_work(writer) 
do_work(painter)
