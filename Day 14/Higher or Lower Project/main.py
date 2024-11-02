from tkinter.font import names

from art import logo, vs
import random
from game_data import data

# Todo 2: Get a random number to pick a competitor
def get_competitor():
    competitor = random.choice(data)
    data.remove(competitor)
    return competitor

def game_judge(chosen, a, b):
    return (chosen == 'a' and a["follower_count"] > b["follower_count"]) or \
           (chosen == 'b' and a["follower_count"] < b["follower_count"])


#Todo 3: Build game spectrum
gaming = True
score = 0
competitor_A = get_competitor()
competitor_B = get_competitor()

while gaming and len(data) > -1:
    print(logo)

    print(f"Compare A: {competitor_A['name']}, a {competitor_A['description']}, from {competitor_A['country']}.")
    print(vs)
    print(f"Compare B: {competitor_B['name']}, a {competitor_B['description']}, from {competitor_B['country']}.")

    choice = ""
    while choice not in ['a', 'b']:
        choice = input("Who was more followers? Type 'A' or 'B': ").lower()

    if game_judge(choice, competitor_A, competitor_B):
        score += 1
        print(f"You're right! Current score: {score}")

        if choice == 'a':
            competitor_B = get_competitor()
        else:
            competitor_A = get_competitor()
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        gaming = False



# Todo 4: Game judgement
