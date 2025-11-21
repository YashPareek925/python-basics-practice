# WAP to find the sum of first n numbers. (using while)

n=int(input("Enter a number:- "))

i=0
s=0
while i<=n:
    s=s+i
    i+=1

print(s)