class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # Protected member

    def _update_marks(self, new_marks):  # Protected method
        self._marks = new_marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self._marks}")

# Example usage
s1 = Student("Alice", 85)
s1.display()
s1._update_marks(92)  # Accessing protected member outside the class
s1.display()