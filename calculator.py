def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("Simple Calculator")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum:", add(x, y))
print("Difference:", sub(x, y))
