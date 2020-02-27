# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:30:49 2020
Fundamentals of Object Oriented Programming (Part1)
@author: jrizos
"""

# Creating a class
# In python the built in solution to the problem we just saw is the class

class Student:
    pass

# we use the keyword class followed by the name of the class.  Once we have the
# class we can start adding attributes.
    

class Student:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname
        
# the __init__ function is a special function used to create an instance of a 
# class. Inside this function we add all the attributes of a class.  The self
# variable represents a variable that refers to the instance of the class that
# you are working with.  Each instance has its own set of attributes.  They are 
# not shared.  
        
class Student:
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname


# create an instance of a class like this
student1 = Student('Niko', 'Rizos')
student2 = Student('Nico', 'Chia')
student3 = Student('Rham', 'Bhaman')

# student1, student2, and student3 are called instances of the Student class

# the type of the student is
print(type(student1))

print('Student 1', student1.first_name, student1.last_name)
print('Student 2', student2.first_name, student2.last_name)
print('Student 3', student3.first_name, student3.last_name)


# what are some other attributes you would add to the Student class?
# Modify the Student class to reflect these new attributes




# Now let's create a parent class, what should a parent have as attributes?

class Parent:
    pass

# Once you create your parent class, lets modify our Student class to take two 
# parents.  When you are done with the Student modifications create your parents
# and add them to your student instance
    


# Now lets create a class that represents a Subject that this student studies.  
# What attributes would you add to this class?  Remember attributes dont have
# to be simple datatypes they can be data structures as well
    
class Subject:
    pass
  
# Once you are done with your Subject class modify your Student to take collection
# of Subjects that the student is taking.  Create your Subjects and add them to 
# your Student
    


# Now lets create a class that represents a Test you take in a SUbject.  What 
# attributes would you add to this class?
    
class Test:
    pass

# Once you are done with the Test, modify your Subject to reflect the Tests the
# Student has taken in that Subject  


# Methods
# If I wanted to create a class that represents a Class this would reasonable

# OOP not only allows us to create classes with attributes but we can also have 
# functions associated with the class
    
class Class:
    def __init__(self, teacher, grade):
        self.teacher = teacher
        self.grade = grade
        self.students = []

    def NumberOfStudents(self):
        return len(self.students)

    def Id(self):
        return str(self.grade) + self.teacher[0]

    def Description(self):
        print('Class:', self.Id())
        print('Teacher:', self.teacher)
        print('Grade:', self.grade)
        print('Num Students:', self.NumberOfStudents())
        
class1 = Class('Krawec', 7)

class1.students.append(student1)
class1.students.append(student2)
class1.students.append(student3)

class1.Description()

# If you look at the code above we have added functions that belong to the class.
# When functions are added to a class they are called methods

# Now I want you to go back to your Subject class and add a method that will calculate
# the average of all the Tests a Student has taken in a Subject

# Inheritance
# The last thing we are going to talk about in OOP is called inheritance.  Just
# like in the biological sense, inheritance is what attributes and methods you 
# inherit from your parents.

# We do this to consolidate common functionality into one class that every child
# class shares
class Student:
    
    def __init__(self):
        self.level = None
        
    def InPreSchool(self):
        return False
    
    def InElementarySchool(self):
        return False
    
    def InHighSchool(self):
        return False

    def StudentLevel(self):
        return self.level
    
# a pre school student inherits from a Student
class PreSchoolStudent(Student):
    def __init__(self):
        self.level = 'Pre School'
        
    def InPreSchool(self):
        return True
    
# a elementary school student inherits from a Student
class ElementarySchoolStudent(Student):
    def __init__(self):
        self.level = 'Elementary School'

    def InElementarySchool(self):
        return True

# a HS school student inherits from a Student
class HighSchoolStudent(Student):
    def __init__(self):
        self.level = 'High School'

    def InHighSchool(self):
        return True

prek_student = PreSchoolStudent()
elementary_student = ElementarySchoolStudent()
hs_student = HighSchoolStudent()

print('PreK Level:', prek_student.StudentLevel())
print('PreK', prek_student.InPreSchool())
print('PreK', prek_student.InElementarySchool())
print('PreK', prek_student.InHighSchool())

print('Elementary Level:', elementary_student.StudentLevel())
print('Elementary', elementary_student.InPreSchool())
print('Elementary', elementary_student.InElementarySchool())
print('Elementary', elementary_student.InHighSchool())

print('HS Level:', hs_student.StudentLevel())
print('HS', hs_student.InPreSchool())
print('HS', hs_student.InElementarySchool())
print('HS', hs_student.InHighSchool())

