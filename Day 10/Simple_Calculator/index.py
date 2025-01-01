import art
import os

# Function to delete the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Adding function
def add(n1, n2):
    return n1 + n2

# Substract function
def subtract(n1, n2):
    return n1 - n2

# Multiply function
def multiply(n1, n2):
    return n2 * n2

# Divide function
def divide(n1, n2):
    return n1 / n2

# Add function to dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# program function
def calculator():

    # Greetings
    print(art.calculator)
    print("Welcome to Simple Calculator Program!")

    should_acc = True
    num1 = float(input("What is the first number?: ")) # first number inputed

    # program looping
    while should_acc: 

        # printing the list of operations
        for symbols in operations:
            print(symbols)

        operation_symbol = input("Pick an operation?: ") # pick the operation
        num2 = float(input("What is the next number?: ")) # input the next number

        ans = operations[operation_symbol](num1, num2) # collect the number and operate

        print(f"{num1} {operation_symbol} {num2} = {ans}") # print the output

        choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation: ").lower() # selector to counting again or no

        # logic if user type y, the program will looping again
        if choice == "y":
            num1 = ans # collect the ans(output) to num1

        else:
            should_acc = False
            clear_screen()
            calculator() # start again the function. it's called recursion

calculator()