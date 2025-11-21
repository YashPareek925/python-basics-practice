# Print the multiplication table of a number n.

n=int(input("Enter a number:- "))

# i=1
# while i<=10:
#     print(n*i)
#     i+=1


for i in range(n, n*11, n):
    print(i)
