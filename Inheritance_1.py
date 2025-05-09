## SINGLE INHERITANCE

# Create a Vehicle class with __init__ that sets brand.
# Then create a Car class that inherits from Vehicle and also sets model.
# Print both brand and model using an object of Car.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) 
        self.model = model

car1 = Car("Toyota", "Hyundai")
print("Brand:", car1.brand)
print("Model:", car1.model)

#============================================================#

## MULTIPLE INHERITANCE

# Create two classes Father and Mother.
# Father sets last_name in __init__.
# Mother sets mother_tongue in __init__.
# Create a Child class that inherits from both and sets first_name.
# Print first name, last name, and mother tongue.

class Father:
    def __init__(self, last_name):
        self.last_name = last_name

class Mother:
    def __init__(self, mother_tongue):
        self.mother_tongue = mother_tongue

class Child(Father, Mother):
    def __init__(self, first_name, last_name, mother_tongue):
        Father.__init__(self, last_name)
        Mother.__init__(self, mother_tongue)
        self.first_name = first_name

child1 = Child("Aariv", "Sharma", "Telugu")
print("First Name:", child1.first_name)
print("Last Name:", child1.last_name)
print("Mother Tongue:", child1.mother_tongue)

#============================================================#

## MULTILEVEL INHERITANCE

# Create a Grandparent class with __init__ that sets family_name.
# Then a Parent class that sets parent_name.
# Then a Child class that sets child_name.
# Print all three using the child class object.

class Grandparent:
    def __init__(self, family_name):
        self.family_name = family_name

class Parent(Grandparent):
    def __init__(self, family_name, parent_name):
        super().__init__(family_name)
        self.parent_name = parent_name

class Child(Parent):
    def __init__(self, family_name, parent_name, child_name):
        super().__init__(family_name, parent_name)
        self.child_name = child_name

child = Child("Priya", "Neha", "Riya")
print("Family Name:", child.family_name)
print("Parent Name:", child.parent_name)
print("Child Name:", child.child_name)

#============================================================#

## HIERARCHICAL INHERITANCE

# Create a Teacher class with __init__ that sets school_name.
# Then create two classes MathTeacher and ScienceTeacher that inherit from Teacher.
# Each one should also set subject.
# Print school name and subject for each.

class Teacher:
    def __init__(self, school_name):
        self.school_name = school_name

class MathTeacher(Teacher):
    def __init__(self, school_name, subject):
        super().__init__(school_name)
        self.subject = subject

class ScienceTeacher(Teacher):
    def __init__(self, school_name, subject):
        super().__init__(school_name)
        self.subject = subject

t1 = MathTeacher("Sun High", "Mathematics")
t2 = ScienceTeacher("Sun High", "Science")

print("Math Teacher:", t1.school_name, "-", t1.subject)
print("Science Teacher:", t2.school_name, "-", t2.subject)

#============================================================#

## HYBRID INHERITANCE

# Create a base class Person that sets name.
# Create a class Employee(Person) that sets employee_id.
# Create another class Student that sets roll_number.
# Now create a class Intern(Employee, Student) that sets `internship_duration

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Student:
    def __init__(self, roll_number):
        self.roll_number = roll_number

class Intern(Employee, Student):
    def __init__(self, name, employee_id, roll_number, internship_duration):
        Employee.__init__(self, name, employee_id)
        Student.__init__(self, roll_number)
        self.internship_duration = internship_duration

intern1 = Intern("Neha", "A123", "R456", "5 months")
print("Name:", intern1.name)
print("Employee ID:", intern1.employee_id)
print("Roll Number:", intern1.roll_number)
print("Internship Duration:", intern1.internship_duration)

#============================================================#

## POLYMORPHISM

# Create two classes: Doctor and Engineer.
# Both should have an __init__ method that sets the person's name.
# Both should have a method work() that prints what they do.
# Doctor.work() → "Dr. [name] is treating patients."
# Engineer.work() → "Engineer [name] is building something."
# Now create a function do_work(person) that calls the work() method of any object passed to it.

class Doctor:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"Dr. {self.name} is treating patients.")

class Engineer:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"Engineer {self.name} is building a bungalow.")

def do_work(person):
    person.work()

d1 = Doctor("Neha")
e1 = Engineer("Sneha")

do_work(d1)  
do_work(e1)  

