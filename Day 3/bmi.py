# input
# converting to float bcs they have a decimal
height = float(input("Input your height: "))
weight = float(input("Input your weight: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
else:  # bmi >= 25
    print("Overweight")
