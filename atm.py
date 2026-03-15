pin = 1234
balance = 5000

entered_pin = int(input("Enter PIN: "))

if entered_pin == pin:
    amount = int(input("Enter amount to withdraw: "))
    
    if amount <= balance:
        print("Withdrawal successful")
        balance = balance - amount
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")