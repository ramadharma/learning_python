# printing new line with 1 print function
print("Hello World \nHello World")

# string manipulation
print("hello" + " " + "rama")

# printing using input() function
print("Hello " + input("What is Your name?") + "!")

# input using variable
name = input("What is Your name?")
lenght = len(name)
print(lenght)

# -------------------------

# Switch the glass
glass1 = "milk"
glass2 = "juice"

# process of switch the glass (bring new glass for temporary storage)
glass3 = glass1
glass4 = glass2

# back to the main glass
glass1 = glass4
glass2 = glass3

print(glass1)
print(glass2)

