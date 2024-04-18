# Write a rock, paper, scissors game
# import random module
import random
# define main function that handles all the logic
def main():
    # define a list of valid choices
    choices = ['rock', 'paper', 'scissors']
    # define a variable to store the user choice
    user_choice = ''
    # define a variable to store the computer choice
    computer_choice = ''
    # define a variable to store the result
    result = ''
    # loop until the user has made a valid choice
    while user_choice not in choices:
        # get the user choice
        user_choice = input('Enter rock, paper, or scissors: ')
    # get the computer choice
    computer_choice = random.choice(choices)
    # determine the result
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
    elif user_choice == 'rock' and computer_choice == 'scissors':
        result = 'You win!'
    elif user_choice == 'paper' and computer_choice == 'rock':
        result = 'You win!'
    elif user_choice == 'scissors' and computer_choice == 'paper':
        result = 'You win!'
    else:
        result = 'You lose!'
    # print the result
    print(f'You chose {user_choice}, the computer chose {computer_choice}. {result}')

    # call main function
    main()