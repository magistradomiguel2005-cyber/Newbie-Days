def add(a, b):
    balance = a 
    rate = b
    total = balance + (balance * rate)
    return total

a = int(input("Enter the balance: "))
b = float(input("Enter the interest rate (as a decimal): "))
print(add(a, b))