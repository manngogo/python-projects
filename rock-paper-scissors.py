import random
rock = 1
paper = 2
scissors = 3

def player():
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    playerchoice = int(input('What do you want to play? 1,2, or 3?'))
    if playerchoice == 1:
        print(f'You chose: rock')
    elif playerchoice == 2:
        print(f'You chose: paper')
    elif playerchoice == 3:
        print(f'You chose: scissors')
    else:
        print('You must select a choice')
        return player()
    return playerchoice

def computer():
    computerchoice = random.randint(1, 3)
    if computerchoice == 1:
        print('Computer chose: rock')
    elif computerchoice == 2:
        print('Computer chose: paper')
    elif computerchoice == 3:
        print('Computer chose: scissors')
    return computerchoice

def game():
    playerchoice = player()
    computerchoice = computer()

    if playerchoice == 1:
        if computerchoice == 1:
            print('You have tied!')
        elif computerchoice == 2:
            print('You have lost!')
        elif computerchoice == 3:
            print('You have won!')
        else:
            print('Error. Please try again later.')
    elif playerchoice == 2:
        if computerchoice == 1:
            print('You have won!')
        elif computerchoice == 2:
            print('You have tied!')
        elif computerchoice == 3:
            print('You have lost!')
        else:
            print('Error. Please try again later.')
    elif playerchoice == 3:
        if computerchoice == 1:
            print('You have lost!')
        elif computerchoice == 2:
            print('You have won!')
        elif computerchoice == 3:
            print('You have tied!')
        else:
            print('Error. Please try again later.')
    else:
        print('Error. Please try again later.')
    print('1. Yes')
    print('2. No')
    gamechoice = int(input('Do you want to play again?'))
    if gamechoice == 1:
        game()
    elif gamechoice == 2:
        print('Thanks for playing!')
    else:
        game()
    print('1. Yes')
    print('2. No')
    gamechoice = int(input('Do you want to play again?'))

game()

