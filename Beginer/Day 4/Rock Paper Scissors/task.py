import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What to you choose? Type 0 for rock, type 1 for paper, type 2 for scissors\n"))
computer = random.randint(0, 2)
if player == 0:
    print(rock)
    print("Computer choose: ")
    if computer == 0:
        print(rock)
        print("Tie")
    elif computer == 1:
        print(paper)
        print("Computer wins")
    elif computer == 2:
        print(scissors)
        print("Player wins")
elif player == 1:
    print(paper)
    print("Computer choose: ")
    if computer == 0:
        print(rock)
        print("Player wins")
    elif computer == 1:
        print(paper)
        print("Tie")
    elif computer == 2:
        print(scissors)
        print("Computer wins")
elif player == 2:
    print(scissors)
    print("Computer choose: ")
    if computer == 0:
        print(rock)
        print("Computer wins")
    elif computer == 1:
        print(paper)
        print("Player wins")
    elif computer == 2:
        print(scissors)
        print("Tie")
