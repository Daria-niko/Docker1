import sys
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

if len(sys.argv) != 4:
    print("Usage: python calc.py <operation> <num1> <num2>")
    print("Operations: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
    sys.exit(1)

# Parse command-line arguments
choice = int(sys.argv[1])
num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

if choice == 1:
    print(num1, "+", num2, "=", addition(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Invalid input")
