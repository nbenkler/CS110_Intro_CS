'''menu.py -- a simple menu-driven program

      Blake Howald 9/19/17, modified from original by Jeff Ondich, 9 April 2009

   This program presents the user with a menu of options.
   After the person types a response, the program calls
   a function to perform the task the person selected.
   This is a small illustration of how to break a big
   problem (present a menu and act according to the user's
   selection) into a collection of smaller ones (print the menu,
   do each operation, etc.) using functions.
'''

import random

def printMenu():
    print('A. Tell me a joke')
    print('B. Sing me a song')
    print('C. Give me a random number from 1 to 10')
    print()

def tellJoke():
    print('Why is 6 afraid of 7?')
    print('Because 7, 8, 9.')
    print()

def singSong():
    print('Two, no six, no twelve')
    print('Baker\'s Dozen!')
    print('I told you that I\'m crazy for these cupcakes cousin.')
    print()

def getRandomIntInRange(n):
    return random.randint(1, n)

def doOperation(selection):
    if selection == 'A':
        tellJoke()
    elif selection == 'B':
        singSong()
    elif selection == 'C':
        print('Here you go:', getRandomIntInRange(10))
        print()
    else:
        print('Please choose A, B, or C next time')
        print()

# The main program begins here.

printMenu()
response = input('Your choice? ')
doOperation(response)

