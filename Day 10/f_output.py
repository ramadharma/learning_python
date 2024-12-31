def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You have not inputing any value"

    """Take a first and last name then format it 
    to return the title case version of the name."""
    formated_f = f_name.title()
    formated_l = l_name.title()

    # the output of the program
    return f"Hello, {formated_f} {formated_l}" 

# called function with return
output = format_name(input("What's first your name? "), input("What's your last name? "))
print(output)

