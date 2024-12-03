import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payer = random.randint(0, 5)
print(f"{friends[payer]} should take the bill.")

print(f"{random.choice(friends)} should take the bill.")