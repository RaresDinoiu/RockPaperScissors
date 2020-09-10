import random

while True:
    choice = str(input("Choose your weapon! "))
    choice = choice.lower()
    print("You chose : ", choice)

    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)

    print("Computer chose ", computer_choice)

    if choice in choices:
        if choice == computer_choice:
            print('It\'s a tie! :| ')
        if choice == 'rock':
            if computer_choice == 'paper':
                 print('You lose! :( ')
            elif computer_choice == 'scissors': #works just as well with an else: instead of elif computer_choice, but it is easier to understand this way
                print('You win! :) ')

        if choice == 'paper':
            if computer_choice == 'scissors':
                 print('You lose! :( ')
            elif computer_choice == 'rock':
                print('You win! :) ')

        if choice == 'scissors':
            if computer_choice == 'rock':
                 print('You lose! :( ')
            elif computer_choice == 'paper':
                print('You win! :) ')
    else:
        print('Wait! That\'s illigal. Choose again!')
    print()

