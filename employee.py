# Define a Employee class with attributes role, department & salary. This class also has showDetails( ) method. 
# Create an Engineer class that inherits properties from Employee & has additional attributes : name & age.

class Employee:
    def __init__(self, role, department, salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print("Role:- ",self.role)
        print("Department:- ",self.department)
        print("Salary:- ",self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def showDetails(self):
        print("Name:- ",self.name)
        print("Age:- ",self.age)
        super().__init__(role, department, salary)
        super().showDetails()

name=str(input("Enter the name of an Employee:- "))
age=int(input("Enter the age of an Employee:- "))
role=str(input("Enter the role of an Employee:- "))
department=str(input("Enter the department of an Employee:- "))
salary=str(input("Enter the salary of an Employee:- "))
eng1=Engineer(name,age)
eng1.showDetails()