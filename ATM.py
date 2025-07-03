#ATM working principle
pin=int(input("Enter your 4 digit pin number:"))
spin=1234
balance=50000
if pin==spin:
    print("Access granted!!")
    withdraw=int(input("Enter amount:"))
    if withdraw>balance:
        print("Insufficient funds!!!")
    else:
        print("Amount withdraw:",withdraw)
        print("Remaining balance:",balance-withdraw)
        print("Thank you for banking with SBI")
else:
    print("Access denied")
    