class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        
student1 = Student("John", 2)
print(f"Student Name: {student1.name}, Roll No: {student1.roll_no}")
