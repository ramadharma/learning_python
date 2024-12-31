import art
import os

# Greetings
print(art.calculator)
print("Welcome to Simple Calculator Program!")

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

# how to called the function with dictionary
test = operations["*"](4, 8)

