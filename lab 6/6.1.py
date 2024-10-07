class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Abhi", 20)
person2 = Person("Akash", 19)

print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")
