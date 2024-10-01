import random

CHOICE_0 = 'Rock'
CHOICE_1 = 'Paper'
CHOICE_2 = 'Scissors'


print(f'Choice 0: {CHOICE_0}\nChoice 1: {CHOICE_1}\nChoice 2: {CHOICE_2}')
comp_choice = random.randint(1, 3)
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))


if comp_choice == user_choice:
    print('It is a Draw. Try again.')
elif comp_choice == 0 and user_choice == 1:
    print(f'Computer choice is {CHOICE_0}. You lose. try again.')
elif comp_choice == 0 and user_choice == 2:
    print(f'Computer choice is {CHOICE_0}. You lose. try again.')
elif comp_choice == 1 and user_choice == 0:
    print(f'Computer choice is {CHOICE_1}. You Won! Bravo!')
elif comp_choice == 1 and user_choice == 2:
    print(f'Computer choice is {CHOICE_1}. You Won! Bravo!')
elif comp_choice == 2 and user_choice == 0:
    print(f'Computer choice is {CHOICE_2}. You Won! Bravo!')
elif comp_choice == 2 and user_choice == 1:
    print(f'Computer choice is {CHOICE_2}. You lose. try again.')



