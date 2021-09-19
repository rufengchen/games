# Paper > rock > scissors, and scissor >paper
import random
def paper_rock_scissor():
    player = input("Rock,scissor,paper! What is your choice? 'r' for rock,\
    'p' for paper, 's' for scissors? ")
    computer = random.choice(['r','p','s'])
    if player == computer:
        print('It\'s a tie.')
    if is_win(player,computer):
        return 'You won!'
    return 'You lost!'
def is_win(x,y):
    # return true if x won
    # r > s, s > p, p > r
    if (x == 'r' and y == 's') or (x == 's' and y == 'p') or (x == 'p' and y == 'r'):
        return True
print(paper_rock_scissor())