print("Welcome to the HelliCoaster!")

height = int(input("What is your height in cm: "))
bill = 0


if height >= 120:
    print("You can ride the HelliCoaster!")
    age = int(input("How old are you: "))
    if age >= 25:
        bill = 20
        print("Older ticket is $20")
    elif age >= 20:
        bill = 18
        print("Young ticket is $18")
    else:
        bill = 15
        print("Childern ticket is $15")
    
    wants_photo =  input("Do you want to want to photo take? Type y for yes, n for no: ")
    if wants_photo == "y":
        bill += 3
        print(f"Your final bill is: ${bill}")

else:
    print("Sorry you can't ride the HelliCoaster..")