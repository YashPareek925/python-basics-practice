# Search for a number x in this tuple using loop:

num=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x=int(input("Enter a number:- "))

for n in num:
    if x==n:
        print(x,"Number is found")
        break
else:
    print("Not found")