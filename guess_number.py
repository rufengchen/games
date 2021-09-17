# Let the computer guess the integer number you have
import random
def guess_num(x):
    low = 1
    high = x
    feedback = ''
    while feedback !='c':
        if low == high:
            guess = high  # low = high
        else:
            guess = random.randint(low,high)
        feedback = input("Is {0} too high(h), too low(l), or correct (c)?".format(guess)).lower()
        if feedback == 'h':
            high = guess - 1
            print("Please guess again!")
        elif feedback == 'l':
            low = guess + 1
            print("Please guess again!")
    print("Here is your number: {0}".format(guess))
guess_num(2)