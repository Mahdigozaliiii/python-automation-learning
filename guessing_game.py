import random
high_score = float("inf")


def play_game():
    global high_score
    print("welcome.")
    print("choose a difficulty game")
    print("easy 1-50")
    print('medium 1-100')
    print("hard 1-500")

    while True:
        level = input("choose your level")
        if level == "1":
            maxnum = 50
            break
        if level == "2":
            maxnum = 100
            break
        if level == "3":
            maxnum = 500
            break
        else:
            print("invalid number")

    secretnumber = random.randint(1, maxnum)
    attempts = 0
    while True:
        try:
            guess = int(input('enter your number'))
            attempts += 1
            if guess < secretnumber:
                print("too low")
            elif guess > secretnumber:
                print("too high")
            else:
                print('you win')
                print(attempts)
                if attempts < high_score:
                    high_score = attempts
                break
        except ValueError:
            print("entter valid number")


if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("paly again:y==yes,n==no")
        if play_again != "y":
            break
