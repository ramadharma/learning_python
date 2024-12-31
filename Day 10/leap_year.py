import os

# Function to delete the screen
def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to check leap or not
def is_leap_year(year):
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Welcome greeting
print("Welcome to leap year checker!")

# Program looping
play = True
while play:

    # input the year and call the function
    input_year = int(input("Please input the year: "))

    # Collect value to the function and print it
    output = is_leap_year(input_year)
    print(f"Is it leap year? {output}")

    # Ask if there are more people to bid
    play_again = input("\nIs there any year to check [Yes/ No]?: ").lower()

    if play_again in ["yes", "y"]:
        clear_screen()  # Clear the screen if they want to continue
    else:
        play = False

