import random
print(''' _______               ___.                    ________                            .__                
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  / 
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/  ''')
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100!")

attempts = 0
answer = random.randint(1, 100)
diff = ""
game_over = False
while diff not in ['easy', 'hard']:
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")

if diff == 'easy':
    attempts = 10
elif diff == 'hard':
    attempts = 5

while not game_over:
    if attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > answer:
            print("Too high.")
            attempts -= 1
        elif guess < answer:
            print("Too low.")
            attempts -= 1
        else:
            print(f"You got it! The answer was {answer}.")
            print("Guess again.")
            game_over = True
    else:
        print("You've run out fo guesses, you loss")
        game_over = True
