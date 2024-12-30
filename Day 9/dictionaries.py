# Dictionary list
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# called dictionary
print(programming_dictionary["Function"])

# adding new list of dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Wipe all list in an existing dictionary
programming_dictionary = {}

# Edit and item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a dictionary
for key in programming_dictionary:
    print(key) # its just giving a key
    print(programming_dictionary[key]) # its giving the value of the key