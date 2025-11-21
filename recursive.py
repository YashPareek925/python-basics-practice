# Write a recursive function to calculate the sum of first n natural numbers.

def naturalSum(num):
    if (num == 0):
        return 0
    
    return naturalSum(num-1) + num
n=int(input("Enter a number:- "))
sum=naturalSum(n)
print(sum)


# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def listPrint(l, index=0):
    if (index == len(l)):
        return
    print(l[index])
    listPrint(l, index +1)

list= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
listPrint(list)