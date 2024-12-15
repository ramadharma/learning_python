import random

# Random integer
random_int = random.randint(5, 10) 
print(random_int)

# Random float
random_0_to_1 = random.random() * 100  # basicly this code the default is 0 - 1, we can add * 10 to create more value
print(random_0_to_1)

random_float = random.uniform(5, 10)
print(random_float)

# Random heads or tails
random_head_or_tail = random.randint(0, 1)
if random_head_or_tail == 0:
    print("Heads")
else:
    print("Tails")