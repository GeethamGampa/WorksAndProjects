# WorksAndProjects
Assignments Done by ME..!!

## Encapsulation
Encapsulation means hiding the internal details of a class and only exposing what is necessary. It protects data by keeping variables private and allowing access through public methods (getters/setters).

## Examples Explained
## 1. Person Class
```
Public variable: name (accessible directly)

Private variable: __age (accessed only via get_age() and set_age() methods)
```
Demonstrates hiding age and controlling access with methods.

## 2. Employee and Manager Classes
```
Protected variable: _salary in Employee (accessible in child class Manager)
```
Shows how protected members can be accessed by subclasses but are not meant to be accessed outside the class hierarchy.

## 3. BankAccount Class
```
Private variable: __balance
```
Methods to safely deposit and withdraw money while ensuring balance never goes negative.

Encapsulation protects balance from direct modification.

## 4. Car Class
```
Public: make

Protected: _model

Private: __price
```
Methods to get/set price and display all attributes.

Shows use of different access levels and controlled access to sensitive data.

## 5. Vehicle and Car (Inheritance)
Vehicle has public, protected, and private variables.

Child class Car can access protected and public directly but accesses private only via methods.

Demonstrates encapsulation combined with inheritance.

## 6. Rectangle Class
```
Private attributes: __width and __height
```
Getters and setters to control dimension changes (validate positive values).

@property used for computed attribute area.

Shows encapsulation with property decorator.

## 7. Employee Class with Annual Salary
```
Private __name and __salary attributes.

Getters and setters to manage them.

annual_salary property calculates salary * 12.
```
Combines encapsulation and computed properties for convenience.

## Key Takeaways
Use private variables (__var) to hide data from outside.

Use protected variables (_var) to indicate variables for subclass use.

Use getter and setter methods to safely access and modify private variables.

Use properties (@property) for computed or controlled access.

Encapsulation protects data integrity and controls how important variables are accessed and modified.

## Abstraction
Abstraction means showing only the important features and hiding the complex details. It helps to simplify the interaction with objects by exposing only relevant methods.

## Inheritance
Inheritance allows a class (child) to inherit properties and methods from another class (parent). It helps to reuse code and create a hierarchy.

## Tuple
A tuple is an ordered, immutable collection of items in Python. Once created, its elements cannot be changed.
```
my_tuple = (1, 2, 3)
```

##  __init__ Method
__init__ is a special method in Python classes. It initializes the object’s attributes when an instance is created.
```
class Person:
    def __init__(self, name):
        self.name = name
```

 MRO (Method Resolution Order)
MRO is the order in which Python looks for a method in a hierarchy of classes (especially with multiple inheritance). It decides which method to call first.

You can check MRO by:
```
print(ClassName.mro())
```

## Multiprocessing
Multiprocessing allows a program to run multiple processes at the same time, using multiple CPU cores. It helps improve performance by parallel execution.

## SQL (Structured Query Language)
SQL is a language used to manage and manipulate relational databases. It allows you to create, read, update, and delete data with commands like SELECT, INSERT, UPDATE, and DELETE.

# School Database with SQLite
This project demonstrates basic SQL operations using Python's sqlite3 module to create and manage a simple school database.

Database Overview
```
Database name: school.db

Table: students

Columns:

id (INTEGER, Primary Key, Auto-increment)

first_name (TEXT)

last_name (TEXT)

address (TEXT)

roll_no (INTEGER)

section (TEXT)
```
## Operations Demonstrated
1. Create Table
Drops existing students table if it exists.

Creates a new students table with specified columns.

2. Insert Records
Inserts 100 student records into the table with sample names, cities, roll numbers, and sections.

Also demonstrates inserting one additional student separately.

3. Select Records
Retrieves and prints all columns for all students.

Retrieves and prints only first and last names of all students.

4. Update Records
Updates the section of a student with a specific roll_no (e.g., roll_no = 10).

5. Delete Records
Deletes a student record with a specific roll_no (e.g., roll_no = 20).

## Key SQL Commands Used
```
CREATE TABLE — Create the table structure

INSERT INTO — Insert new rows

SELECT — Query data

UPDATE — Modify existing data

DELETE — Remove rows

DROP TABLE IF EXISTS — Delete table if it exists (to reset)
```
