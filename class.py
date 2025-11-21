# Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, marks1, marks2, marks3):
      self.name=name
      self.marks1=marks1
      self.marks2=marks2
      self.marks3=marks3

    def avg(self):
       sum=(self.marks1+self.marks2+self.marks3)/3
       print(sum)
      

s1=Student("Yash",79, 45, 65)
s1.avg()