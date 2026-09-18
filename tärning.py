import random
ditt_slag = random.randint(1,6)
datorns_slag = random.randint(1,6)
print(f"Du slog: {ditt_slag}")
print(f"Datorn slog: {datorns_slag}")
if ditt_slag > datorns_slag:
    print("Du vann!")
else:
    print("Datorn vann den här gången.")