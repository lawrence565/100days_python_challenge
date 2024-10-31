# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
print("Welcome to the secret auction program.")

keep_bidding = True
bid_dict = {}
while keep_bidding:
    name = input("What is your name? ")
    bid = int(input("WHat's the bid? $"))
    bid_dict[name] = bid
    option = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if option == 'no':
        keep_bidding = False
    elif option == "yes":
        print("\n" * 20)

max_bid = 0
winner = ""
for bidder in bid_dict:
    if bid_dict[bidder] > max_bid:
        winner = bidder
        max_bid = bid_dict[bidder]

print(f"The winner is {winner} with a bid of ${max_bid}.")

