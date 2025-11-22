import random

passLength=int(input("Enter length of password:- "))
randpass=""
val="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
for password in range(passLength):
    randpass += random.choice(val)

print("Your random password:-", randpass)