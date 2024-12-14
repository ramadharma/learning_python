# input
# converting to float bcs they have a decimal
height = float(input("Input your height: "))
weight = float(input("Input your weight: "))

bmi = weight / (height ** 2)

print(f"Your bmi is: {str(round(bmi, 2))}")