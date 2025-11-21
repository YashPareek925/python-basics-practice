# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks={}

m=int(input("Enter marks of Physics:- "))
marks.update({"Physics": m})
m=int(input("Enter marks of Chemistry:- "))
marks.update({"Chemistry": m})
m=int(input("Enter marks of Maths:- "))
marks.update({"Maths": m})

print(marks)