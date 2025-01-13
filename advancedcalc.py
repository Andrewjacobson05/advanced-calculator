import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def exponentiate(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error! Cannot take the square root of a negative number."
    return math.sqrt(a)

def logarithm(a, base=10):
    if a <= 0:
        return "Error! Logarithm is undefined for non-positive numbers."
    return math.log(a, base)

def calculator():
    print("Welcome to the Advanced Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation (a^b)")
    print("6. Square Root")
    print("7. Logarithm (base 10 by default)")

    while True:
        try:
            choice = int(input("Enter choice (1-7): "))
            if choice in [1, 2, 3, 4, 5]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == 1:
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == 2:
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == 3:
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == 4:
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
                elif choice == 5:
                    print(f"Result: {num1} ^ {num2} = {exponentiate(num1, num2)}")

            elif choice == 6:
                num = float(input("Enter a number: "))
                print(f"Result: √{num} = {square_root(num)}")

            elif choice == 7:
                num = float(input("Enter a number: "))
                base = input("Enter base (press Enter to use base 10): ")
                if base == "":
                    print(f"Result: log({num}) = {logarithm(num)}")
                else:
                    print(f"Result: log base {base} of {num} = {logarithm(num, float(base))}")

            else:
                print("Invalid input. Please enter a number between 1 and 7.")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                print("Thank you for using the Advanced Calculator!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculator()