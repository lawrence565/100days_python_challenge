import random
from art import logo
print(logo)

def deal_card():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    card = random.choice(cards)
    return card

def sum_card(hands):
    point = 0
    for hand in hands:
        if hand == 'A':
            point += 1
        elif hand == "J" or hand == "Q" or hand == "K":
            point += 10
        else:
            point += int(hand)
    if 'A' in hands:
        if point + 10 <= 21:
            point += 10
    return point

play = None
while play is not True:
    playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if playing == 'y':
        play = True
    elif playing == 'n':
        play = False

    while play is True:
        player_card = []
        computer = []
        for _ in range(2):
            player_card.append((deal_card()))
            computer.append((deal_card()))

        player_point = sum_card(player_card)
        computer_point = sum_card(computer)
        print("Your cards: " + str(player_card) + ", current score is " + str(player_point))
        print("Computer's first cards: " + computer[0])

        keep_getting_card = True
        while keep_getting_card:
            next_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if next_card == 'y':
                player_card.append(deal_card())
                player_point = sum_card(player_card)
                print("Your cards: " + str(player_card) + ", current score is " + str(player_point))
            else:
                keep_getting_card = False
        while computer_point != 0 and computer_point <= 17:
            computer.append(deal_card())
            computer_point = sum_card(computer)

        print("Your final hand: " + str(player_card))
        print("Computer's final hand: " + str(computer))

        if player_point > 21:
            print("You Lose")
        elif computer_point > 21:
            print("You Win")
        elif 21 - player_point < 21 - computer_point:
            print("You Win")
        else:
            print("You Lose")
        play = None