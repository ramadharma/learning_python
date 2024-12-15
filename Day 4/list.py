state_of_tulungagung = ["Tulungagung", "Kauman", "Boyolangu", "Besuki"]

# Change the name of the list item
state_of_tulungagung[1] = "Cauman"

# Add more item to the list (will be add in the last of the list)
state_of_tulungagung.append("Campurdarat") # add for single item
state_of_tulungagung.extend(["Ngantru", "Ngunut"]) # add for multi item 

print(state_of_tulungagung)