class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display_person_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
class Employee(Person):
    def __init__(self, name, age,employee_id,salary):
        super().__init__(name, age)    
        self.employee_id=employee_id
        self.salary=salary
    
    def display_employee_info(self):
        self.display_person_info()
        print("Employee id:",self.employee_id)
        print("Salary:",self.salary)
    
name=str(input("Enter name:"))
age=int(input("Enter age:"))
employee_id=int(input("Employee id:"))
salary=int(input("Salary:"))

emp=Employee(name,age,employee_id,salary)
emp.display_employee_info()