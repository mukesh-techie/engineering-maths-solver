# Engineering Maths Solver
# Made by: Mukesh Kumar Dhivakar
# For engineering students!

import cmath  # handles complex numbers too, not just real ones


def quadratic(a, b, c):
    """Solve ax^2 + bx + c = 0"""
    if a == 0:
        print("Not a quadratic equation (a cannot be 0). It's linear: bx + c = 0")
        if b != 0:
            x = -c / b
            print(f"x = {x}")
        else:
            print("No valid equation (a and b are both 0).")
        return

    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        print(f"Two real roots: x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x = -b / (2*a)
        print(f"One real root (repeated): x = {x}")
    else:
        # use cmath so we actually show the complex roots, not just say "complex"
        x1 = (-b + cmath.sqrt(d)) / (2*a)
        x2 = (-b - cmath.sqrt(d)) / (2*a)
        print(f"Complex roots: x1 = {x1}, x2 = {x2}")


def matrix_det(a, b, c, d):
    """Determinant of a 2x2 matrix [[a, b], [c, d]]"""
    det = (a * d) - (b * c)
    print(f"Determinant = {det}")


def get_float(prompt):
    """Keep asking until the user enters a valid number — avoids crashing on bad input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number, please try again.")


def main():
    while True:
        print("\n=== Engineering Maths Solver ===")
        print("1. Quadratic Equation")
        print("2. Matrix Determinant (2x2)")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            a = get_float("Enter a: ")
            b = get_float("Enter b: ")
            c = get_float("Enter c: ")
            quadratic(a, b, c)

        elif choice == "2":
            print("Enter 2x2 matrix values:")
            a = get_float("a: ")
            b = get_float("b: ")
            c = get_float("c: ")
            d = get_float("d: ")
            matrix_det(a, b, c, d)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
