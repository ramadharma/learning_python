print("Welcome to Pappa Pizza!")

size = input("What size do you want? S, M, or L: ")

pizza_price = 0

if size == "S":
    pizza_price = 15
    print(f"The price for S size is ${pizza_price}")

    # Add pepperoni
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        pizza_price += 2
        print("The charge for adding pepperoni is $2")

     # Add extra cheese
    cheese = input("Do you want extra cheese on your pizza? Y or N: ")
    if cheese == "Y":
        pizza_price += 1
        print(f"Your final bill is ${pizza_price}")
    
    else:
        print(f"Your final bill is ${pizza_price}")

elif size == "M":
    pizza_price = 20
    print(f"The price for M size is ${pizza_price}")

    # Add pepperoni
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        pizza_price += 3
        print("The charge for adding pepperoni is $3")

     # Add extra cheese
    cheese = input("Do you want extra cheese on your pizza? Y or N: ")
    if cheese == "Y":
        pizza_price += 1
        print(f"Your final bill is ${pizza_price}")
    
    else:
        print(f"Your final bill is ${pizza_price}")

elif size == "L":
    pizza_price = 25
    print(f"The price for L size is ${pizza_price}")

    # Add pepperoni
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == "Y":
        pizza_price += 3
        print("The charge for adding pepperoni is $3")

     # Add extra cheese
    cheese = input("Do you want extra cheese on your pizza? Y or N: ")
    if cheese == "Y":
        pizza_price += 1
        print(f"Your final bill is ${pizza_price}")
    
    else:
        print(f"Your final bill is ${pizza_price}")

else:
    print("We don't have that pizza type")

    