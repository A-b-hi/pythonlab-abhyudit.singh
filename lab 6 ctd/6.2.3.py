class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id  # Public member
        self._name = name  # Protected member
        self.__salary = salary  # Private member

    # Public method
    def get_details(self):
        print(f"Employee ID: {self.emp_id}, Name: {self._name}, Salary: {self.__salary}")

    # Protected method
    def _set_name(self, new_name):
        self._name = new_name

    # Private method
    def __set_salary(self, new_salary):
        self.__salary = new_salary

    def update_salary(self, new_salary):
        self.__set_salary(new_salary) 

emp = Employee(101, "John Doe", 50000)
emp.get_details()
emp._set_name("John Smith")  
emp.update_salary(55000) 
emp.get_details()