# calculator.py
# Author: Abdul Azim
# Description: A simple console-based calculator with basic and scientific functions.

import math
import os


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_number(prompt):
    """Safely takes a numeric input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def basic_calculator():
    """Performs basic arithmetic operations."""
    while True:
        print("\n--- Basic Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Back to Main Menu")

        choice = input("\nSelect an option (1-6): ")

        if choice == '6':
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} × {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} ÷ {num2} = {num1 / num2}")
            elif choice == '5':
                if num2 == 0:
                    print("Error: Modulus by zero is not allowed.")
                else:
                    print(f"Result: {num1} % {num2} = {num1 % num2}")
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")
        clear_screen()


def scientific_calculator():
    """Performs scientific calculations."""
    while True:
        print("\n--- Scientific Calculator ---")
        print("1. Square Root")
        print("2. Power (x^y)")
        print("3. Trigonometric Functions (sin, cos, tan)")
        print("4. Factorial")
        print("5. Back to Main Menu")

        choice = input("\nSelect an option (1-5): ")

        if choice == '5':
            break

        if choice == '1':
            num = get_number("Enter a number: ")
            if num < 0:
                print("Error: Square root of a negative number is not supported.")
            else:
                print(f"Result: √{num} = {math.sqrt(num)}")

        elif choice == '2':
            base = get_number("Enter base: ")
            exponent = get_number("Enter exponent: ")
            print(f"Result: {base}^{exponent} = {math.pow(base, exponent)}")

        elif choice == '3':
            angle = get_number("Enter angle in degrees: ")
            radians = math.radians(angle)

            print(f"sin({angle}) = {math.sin(radians)}")
            print(f"cos({angle}) = {math.cos(radians)}")

            if math.cos(radians) == 0:
                print("tan is undefined for this angle.")
            else:
                print(f"tan({angle}) = {math.tan(radians)}")

        elif choice == '4':
            num = get_number("Enter a non-negative integer: ")
            if num < 0 or not num.is_integer():
                print("Error: Factorial is defined only for non-negative integers.")
            else:
                print(f"Result: {int(num)}! = {math.factorial(int(num))}")

        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")
        clear_screen()


def main():
    """Main program loop."""
    while True:
        clear_screen()
        print("=" * 35)
        print("        CALCULATOR PROGRAM")
        print("        Developed by Abdul Azim")
        print("=" * 35)

        print("\n1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Exit")

        choice = input("\nSelect an option (1-3): ")

        if choice == '1':
            basic_calculator()
        elif choice == '2':
            scientific_calculator()
        elif choice == '3':
            print("\nProgram terminated.")
            break
        else:
            print("Invalid input. Please select 1, 2, or 3.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()