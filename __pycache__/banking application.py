balance = 1000

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        return balance
    else:
        return "Insufficient balance"

def check_balance():
    return balance


print("Initial balance:", check_balance())

deposit(500)
print("After deposit:", check_balance())

withdraw(300)
print("After withdrawal:", check_balance())