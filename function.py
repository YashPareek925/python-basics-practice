# WAF to print the length of a list. ( list is the parameter)

# def calLength(n):
#     print(len(n))

# num=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# calLength(num)


# WAF to print the elements of a list in a single line. ( list is the parameter)

# def printList(n):
#     for i in n:
#         print(i, end=" ")

# printList(num)


# WAF to find the factorial of n. (n is the parameter)

# def fac(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     print(f)

# n=int(input("Enter a number:- "))
# fac(n)

# WAF to print number into string wether its Even or Odd

def evenOdd(num):
    for i in num:
        if (i % 2 == 0):
            print("Even")

        else:
            print("Odd")
        
n=int(input("Enter a number:- "))
evenOdd(n)