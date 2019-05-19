import random
import math

def reminder(num, hint_num):
    calculate_reminder = 10%num
    print(f'Hind {hint_num}: Output of (10 % guess) is {calculate_reminder}')

def addition(num, hint_num):
    random_add = random.randint(11,20)
    calculate_addition = random_add + num
    print(f'Hind {hint_num}: If you add ({random_add} + guess), output will be {calculate_addition}')

def power(num, hint_num):
    calculate_power = num ** 2
    print(f'Hind {hint_num}: Power of (guess) is {calculate_power}')

print('''
------------------------------------------------
     Welcome to the game of guessing number
------------------------------------------------
Rule: You will get 2 hints to guess the secret number between 1 to 9
''')

while True:

    secret_number = random.randint(1,9)

    # Get random hind function
    hint_functions = {reminder,addition,power}
    random_hints = random.sample(hint_functions, 2)

    # Show random hints
    for hint in random_hints:
        sr_number = random_hints.index(hint) + 1
        hint(secret_number, sr_number)

    guess_count = 0
    guess_limit = 3

    '''
        Ask to user guess number
    '''
    print(" ")
    print("Guess your number\n-----------------")
    while guess_count < guess_limit:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess == secret_number:
            print("Congratulations! You won")
            break
    else:
        print("Sorry, you failed!")
        print(f'Number is : {secret_number}')

    play_again = input("Do you want to play again? (Y/N) : ")
    if play_again.upper() != 'Y':
        break
