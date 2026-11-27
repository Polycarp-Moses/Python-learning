# CLASS VARIABLES IN PYTHON

# Class variables are shared among all instances(objects) created from a class a class. 
# While instance variables are defined inside the constructor, class are defined outside the constructor.
#Example: 
class car:
    wheels = 4 #class variable
    def __init__(self, model, year):
        self.model = model #instance variable
        self.year = year  #instance variable

# Class variables allow you to share data among all objects created from that class. While with instance variables, each object has their own version. With class variables, all those objects share one variable. 

class Student:

    class_year = 2024
    num_students = 0 # you can add other class variables

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # we can write any code we want within our constructor. This code increases the number of students by 1 each time we create a new student object. 

student1 = Student("Moses", 34)
student2 = Student("Patrick", 35)
student3 = Student("Kamau", 40)
student4 = Student("Sandy", 27)

print(student1.name)
print(student1.age)
print(student1.class_year, "\n") #accessing the class variable through the object student1.

#its good practice to access a class variable through the class name itself rather than the objects. This helps with clarity and readability. 

print(student2.name)
print(student2.age)
print(Student.class_year, "\n")

# We can have multiple class variables
print(Student.num_students, "\n")

#Exercise: Print class year and number of students
print(f"My graduating class of {Student.class_year} has {Student.num_students} students:")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)


