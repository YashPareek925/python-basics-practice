import random
randNum=random.randint(1,100)

while True:
    userNum=int(input("Guess a number:-"))

    if randNum==userNum:
        print("Your guess is correct. So the game is over!!")
        break

    elif randNum < userNum:
        print("Your number is bigger than the target.Guess again")

    else:
        print("Your number is smaller than the target.Guess again")