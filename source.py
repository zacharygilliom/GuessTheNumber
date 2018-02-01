import random

x = random.randint(0, 150)


game_end = False


def check_accuracy():
    if your_number.isnumeric():
        print("Why would you pick THAT number?\n")
    else:
        print("You must choose an actual number\n")
    return


def check_high_or_low():
    if int(your_number) > x:
        print("Your guess is WAY too high\n")
        game_end = False
    if int(your_number) < x:
        print("Your guess is WAY too low\n")
        game_end = False
    if int(your_number) == x:
        print("Hey idiot you actually got the number correct\n")
        game_end = True
    return game_end


def check_difference():
    y = abs(x - int(your_number))
    print("You guessed a number that is " + str(y) + " away from the actual number\n")
    return


while game_end == False:
    your_number = input("Please guess what you think the number is\n")
    check_accuracy()
    check_difference()
    a = check_high_or_low()
    if a:
        break








