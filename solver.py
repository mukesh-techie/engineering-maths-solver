# Engineering Maths Solver
# Made by: Your Name
# For engineering students!

import math

def quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x = -b/(2*a)
        print(f"x = {x}")
    else:
        print("Complex roots!")

def matrix_det(a,b,c,d):
    det = (a*d) - (b*c)
    print(f"Determinant = {det}")

print("=== Engineering Maths Solver ===")
print("1. Quadratic Equation")
print("2. Matrix Determinant")
choice = input("Enter choice: ")

if choice == "1":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    quadratic(a, b, c)
elif choice == "2":
    print("Enter 2x2 matrix values:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = float(input("d: "))
    matrix_det(a,b,c,d)
