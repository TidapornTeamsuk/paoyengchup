#pao yeng chup

import random

def play(player):
    # x = ('r','p','s')
    y = {'r': 'rock', 'p':'paper','s':'scissors'}

    computer = random.choice(list(y.keys()))
    # computer = x[random.randrange(len(x))]

    if player == computer:
        result = 'tie'
    elif player == 'r' and computer == 's':
        result = 'you win'
    elif player == 'p' and computer == 'r':
        result = 'you win'
    elif player == 's' and computer == 'p':
        result = 'you win'
    else:
        result = 'you lose'
    print('you : {} <-> computer : {} => {}'. format(y[player], y[computer], result))

while True:
    player = input('[r]ock, [p]aper, [s]cissors, [e]xit ->')
    if player == 'e':
        break
    else:
        play(player)