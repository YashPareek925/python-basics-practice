# WAF to convert USD to INR.

usd=float(input("Enter USD:- "))

def USDtoINR(usd):
    inr=usd*88.74
    print (f"{inr:.2f}")

USDtoINR(usd)