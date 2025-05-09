# create a database for school - 100 rows
# attributes/col: id, surname, name, address, roll_no, section

# insert 
# select
# update
# delete

# ======================================================================================#
# ======================================================================================#

import sqlite3

# Connect to the database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# To reset every time
cursor.execute('DROP TABLE IF EXISTS students') # Remove the whole table

# Create the table
# AUTOINCREMENT : gives a new number for each new row
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        address TEXT NOT NULL,
        roll_no INTEGER NOT NULL,
        section TEXT NOT NULL
    )
''')


first_names = ["Geetham", "Harish", "Anjali", "Ravi", "Neha", "Amit", "Sita", "Krishna", "Divya", "Arjun"]
last_names = ["Gampa", "Surla", "Sharma", "Kumar", "Reddy", "Yadav", "Rao", "Patil", "Jain", "Mehta"]
cities = ["Hyderabad", "Mumbai", "Delhi", "Bengaluru", "Chennai", "Vizag", "Pune", "Jaipur", "Kolkata", "Bhopal"]
sections = ['A', 'B', 'C', 'D']

# Insert 100 students
for i in range(1, 101):
    # loop through the list of names, cities, sections
    first_name = first_names[i % len(first_names)] # eg: 1%10 =0, 2%10 = 2.......11%10 = 1
    last_name = last_names[i % len(last_names)]
    city = cities[i % len(cities)]
    section = sections[i % len(sections)]
    roll_no = i # current value in the loop

   
   # ------------------ INSERT ------------------ #
    cursor.execute('''
        INSERT INTO students (first_name, last_name, address, roll_no, section)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, city, roll_no, section))

# Save the changes
conn.commit()

# Show all students
# ------------------ 1st SELECT ------------------ #
cursor.execute('SELECT * FROM students')

rows = cursor.fetchall()
for row in rows:
    print(row)
    
# ------------------ 2nd SELECT ------------------ #
cursor.execute('SELECT first_name, last_name FROM students')

rows = cursor.fetchall()
for row in rows:
    print(row)


# ======================================================================================#
# ======================================================================================#

# ------------------ INSERT ------------------ #
# Insert one more student 
cursor.execute('''
    INSERT INTO students (first_name, last_name, address, roll_no, section)
    VALUES (?, ?, ?, ?, ?)
''', ("Lakshmi", "Verma", "Ahmedabad", 101, "A"))

# Commit and print the newly added student
conn.commit()

cursor.execute('SELECT * FROM students WHERE roll_no = 101')
print(cursor.fetchone())


# ------------------ UPDATE ------------------ #
# Update a student's section based on roll_no
# SET used to assign a new value to a column
cursor.execute('''
    UPDATE students 
    SET section = ? 
    WHERE roll_no = ?
''', ('A', 10))

conn.commit()

# ------------------ DELETE ------------------ #
# Delete a student based on roll_no
cursor.execute('''
    DELETE FROM students 
    WHERE roll_no = ?
''', (20,))

conn.commit()

# After update and delete 
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()
print("\nAll students after UPDATE and DELETE:")
for row in rows:
    print(row)

conn.close()