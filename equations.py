def create_equation(a, b, c):
    equation = ((a + b + c) * (a - b - c) * (a * b) + (a ** 2) + (b ** 2) + (a * b * c) ** 3)
    return equation


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

print(create_equation(a, b, c))
