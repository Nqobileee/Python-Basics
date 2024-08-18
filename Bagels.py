# This is a game called bagels

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():

# The {} means a value you have declared before will be entered when running the code
# In this case we said .format(NUM_DIGITS) so the value declared for NUM_DIGITS will be entered
    
    print(''' Bagels, a deductive logic game.
          I am thinking of a {}-digit number with no repeated digits. 
          Try to guess what it is. Here are some clues:
          When I say: That means:
            Pico    One digit is correct but in the wrong position.
            Fermi   One digit is correct and in the right position.
            Bagels  No digit is correct.
          
          For example, if the secret number was 248 and your guess was 843, clues would be Fermi Pico. '''.format(NUM_DIGITS))
    
    # while loop is used to repeatedly execute a block of code as long as the condition is true
    while True: 
        secretNum = getSecretNum()
        print('I have thought of a number.')

        # {} value was used again, meaning we are gonna get a value stated before

        print('You have {} guesses to get to it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses> MAX_GUESSES:
                print('You ran out o guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Thanks for playing!')


def getSecretNum():
    
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''

    # for loop is best used when a number of iterations are known already like a list or a range
    # Unlike a while loop typically used when the number of iterations isnt predetermined and depends on a condition being met

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess[i] == secretNum[i]:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:

            # append is used to add an item to the end of a list
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
        
        # len is used to determine length of a list

        if len(clues) == 0:
            return 'Bagels'
        else:
            clues.sort()
            return''.join(clues)

__name__ == '_main_'
main()




