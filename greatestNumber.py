# WAP to find the greatest of 3 numbers entered by the user.

num1=float(input("Enter first number:- "))
num2=float(input("Enter second number:- "))
num3=float(input("Enter third number:- "))

if(num1>=num2 and num1>=num3):
    print("First number is greater.")

elif(num2>num3):
    print("Second number is greater.")

else:
    print("Third number is greater")