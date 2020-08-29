import random

def guess_word()-> None:
    """Make a user try to guess a randomly selected word from a list of words in three trys
    """

    words_list = ['apple', 'banana', 'mango', 'orange', 'guava', 'pineapple', 'fig', 'pawpaw', 'strawberry']
    fruit = random.choice(words_list)
    tries = 0

    print(f'From this fruit : {words_list} guess my fruit')
    print('You have only three tries.\n')
    while True:
        guess = str(input('Enter a your :'))
        tries += 1
        if guess == fruit:
            print(f'Hooray! weldone, {guess} is the fruit.\n')
            break
        else :
            print(f'Sorry {guess} is not the fruit')
            print(f'You have {3 - tries} remaining\n')
        if tries == 3:
            print(f'Sorry times up, the fruit is : {fruit}\n')
            break
guess_word()
