# Search for a number x in this tuple using loop:

tup=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x=int(input("Enter element to search:- "))

i=0
while i<= len(tup)-1:
    if x==tup[i]:
        print("Found at index",i)
    else:
        print("Not found")

    i+=1