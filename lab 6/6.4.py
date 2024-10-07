class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)
student2 = Student("Bob", 21)

print(f"Student Name: {student1.name}, Age: {student1.age}")
print(f"Student Name: {student2.name}, Age: {student2.age}")
