def calculate_love_score(name1, name2):
    
    # Combine the two names into a single string
    combined_names = name1 + name2
    # Convert the combined string to lowercase to make the letter counting case-insensitive
    lower_names = combined_names.lower()
    
    # Count the occurrences of each letter in the word "TRUE"
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    # Sum up the counts to form the first digit of the score
    first_digit = t + r + u + e
    
    # Count the occurrences of each letter in the word "LOVE"
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")  # Note: "e" is counted again here
    # Sum up the counts to form the second digit of the score
    second_digit = l + o + v + e
    
    # Combine the first and second digits into a two-digit score
    score = int(str(first_digit) + str(second_digit))
    return score

# Example call to the function
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
score = calculate_love_score(name1, name2)
print(f"Your love score is {score}.")
