# WAP to check if a list contains a palindrome of elements.

list1=[1,2,2,1]
copylist=list1.copy()
copylist.reverse()
if (list1==copylist):
    print("list is palindrome.")

else:
    print("list is not a palindrome.")
