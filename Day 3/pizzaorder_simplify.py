print("Welcome to Pappa Pizza!")

size = input("What size do you want? S, M, or L: ")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

cheese = input("Do you want extra cheese on your pizza? Y or N: ")

bill = 0

# Choose the size
if size == "S":
    bill = 15

elif size == "M":
    bill = 20

elif size == "L":
    bill = 25

else:
    print("We don't have that pizza type")

# Workout total bill based on adding pepperoni or no
if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or "L":
        bill += 3

# Workout total based on adding extra cheese or no
if cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")