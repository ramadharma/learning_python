import random

friends = ["Aaliyah", "Budi", "Sari", "Maimunah", "Zaki"]

# Option 1
print(random.choice(friends))

# Option 2
random_index = random.randint(0, 4)
print(friends[random_index])