print("Welcome to the tip calculator!")

# Input total
total_bill = float(input("What was the total bill? $"))

# Input tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Input people
people = int(input("How many people to split the bill? "))

# math
total_tip = float(total_bill * tip / 100)
total_pay = ((total_bill + total_tip) / people)

# final print
print(f"Each person should pay: ${round(total_pay, 2)}") 