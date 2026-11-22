import random


def play_game():
    print("welcome.choose a number 1 - 100")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("enter your guess"))
            attempts += 1
            if guess < secret_number:
                print("low")
            elif guess > secret_number:
                print("high")
            else:
                print("you win")
                break
        except ValueError:
            print('not valid')


play_game()
