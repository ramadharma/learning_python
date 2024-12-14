print("Welcome to Odd or Even")

number = int(input("Please input your number: "))

# Math checker
checker = number % 2

# logic
if checker == 1:
    print("Your number is Odd")
else:
    print("Your number is Even")