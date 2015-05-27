#Sam Verma
#Bagels number guessing game
#comes up with a random number of a set number of digits for user to guess

import random

def generateNum(numDigits):
    #returns string made up of numDigits random digits
    digits = list(range(10))
    random.shuffle(digits)
    target=''
    for i in range(numDigits):
        target+=str(digits[i])
    return target

def hints(guess,target):
    #returns string with fermi, pico, and bagels hints
    if guess==target:
        return 'You got it!'

    hint=[]

    for i in range(len(guess)):
        if guess[i]==target[i]:
            hint.append('Fermi')
        elif guess[i] in target:
            hint.append('Pico')

    if len(hint)==0:
        return 'Bagels'

    hint.sort()
    return ''.join(hint)

def isDigits(num):
    #returns true if num is string of only digits
    if num=='':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def playAgain():
    #returns true if user wants to play again
    print('Play again? (yes or no)')
    print()
    return input().lower().startswith('y')

NUMDIGITS=3
GUESSLIMIT=10

print('I\'m thinking of a %s digit number. Try to guess what it is.' % (NUMDIGITS))
print()
print('I\'ll give the following hints:')
print('Pico - when one digit is correct but in the wrong position')
print('Fermi - when one digit is correct and in the right position')
print('Bagels - when no digit is correct')
print()
while True:
    target=generateNum(NUMDIGITS)
    print('I have thought of a number. You have %s guesses to get it.' % (GUESSLIMIT))
    print()
    numGuess=1
    while numGuess<=GUESSLIMIT:
        guess=''
        while len(guess)!=NUMDIGITS or not isDigits(guess):
            print('Guess #%s: '%(numGuess))
            guess=input()

        clue=hints(guess,target)
        print(clue)
        print()
        numGuess+=1

        if guess==target:
            break
        if numGuess>GUESSLIMIT:
            print('You have run out of guesses. The answer was %s.'%(target))

    if not playAgain():
        break
