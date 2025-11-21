# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, bal, acc, inp):
        self.bal=bal
        self.acc=acc
        self.inp=inp
        bal=self.bal

        if self.inp=='1':
            self.debit()
        elif self.inp=='2':
            self.credit()
        elif self.inp=='3':
            self.printBal()
        else:
            print("Invalid input")

    def debit(self):
        deb=float(input("Enter the amount to debit:-"))
        self.bal= self.bal - deb
        self.printBal()
    
    def credit(self):
        cre=float(input("Enter the amount to credit:-"))
        self.bal= self.bal + cre
        self.printBal()
    
    def printBal(self):
        print("Your current balance is:-", self.bal)


print("\nWhat do you want?")
print("1. Debit")
print("2. Credit")
print("3. Check Balance")
inp= input("Enter your choic:- ")

acc1=Account(5000,75864253, inp)