import random 

def guessing_game()-> None:
    '''Make a user guess a randomly generated number from 1 to 100(inclusive).
    '''
    answer = random.randint(1, 100) # answer contains a randomly generated number
    
    while True: # infinite loop that provides checking to the user's guess
        guess = int(input('What is your guess : '))
        
        if guess == answer:
            print(f'Your guess of {guess} is correct')
            break # if guess is correct print message and end program

        # if guess is not correct print suitable message and ask for another guess
        if guess < answer:
            print(f'Your guess of {guess} is lower than the number')
        if guess > answer:
            print(f'Your guess of {guess} is higher than the answer')

if __name__ == '__main__':
    guessing_game()
