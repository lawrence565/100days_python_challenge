print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S" or size == "s":
    if pepperoni == "Y":
        bill += 17
    elif pepperoni == "N":
        bill += 15
    else:
        print("Wrong choice")
elif size == "M" or size == "m":
    if pepperoni == "Y":
        bill += 23
    elif pepperoni == "N":
        bill += 20
    else:
        print("Wrong choice")
elif size == "L" or size == "l":
    if pepperoni == "Y":
        bill += 28
    elif pepperoni == "N":
        bill += 25
    else:
        print("Wrong choice")
else:
    print("Wrong input")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")