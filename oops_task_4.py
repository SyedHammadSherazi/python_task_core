# Add a __str__ method so that print(student) gives readable output

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student: {self.name}, {self.age} years old"

student_pri = Student("hammad", 26)
print(student_pri)  

