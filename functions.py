#Example 1
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
def find_bigger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Both are equal"
print("Bigger number is:",find_bigger(a, b))

#Example 2
x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "cannot divide by Zero"
print("Result:",safe_divide(x, y))

#Example 3
total = 10
x = int(input("Enter count remaining to get Final total: "))
def update_total(x):
    global total
    total += x
    return total
print("Final total is:",update_total(x))
