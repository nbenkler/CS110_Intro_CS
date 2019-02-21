'''strings0.py

   Originally created by Jeff Ondich (2009), modified by Blake Howald (9/8/17)

   This sample program will introduce you to some simple operations
   on strings in Python.  There are questions in the comments below.
   Try to answer them.  When you have questions of your own, try
   experimenting to figure out the answers.
'''

# Double quotes versus single quotes.
#
# -- You can specify a string in Python using either single quotes (apostrophes)
#      or double quotes.  I normally use single-quotes, but in the second print
#      statement below, I used double quotes.  Why was that necessary?
# -- What does a "print" alone on a line do?

print('Welcome to strings0.')
print("What's the reason for using single-quotes sometimes and double-quotes others?")
print()


# Commas in print statements.
#
# -- What happens when you separate two strings by a comma in a
#      print statement?
# -- What happens when you end a print statement witha comma?

print('What', 'year', 'is', 'it?')
print('The year is',)
print('2017.')
print()


# Concatenation: the "+" operator with strings.
#
# -- What does the plus sign do when placed between two strings?
# -- Can you combine three or more strings with plus signs?

s = 'Agent'
t = 'Cooper'
print('The separate strings are', s, 'and', t)
print('The combined string is', s + t)
print()


# Input.
#
# -- Why put a space after the question mark below?
# -- Don't worry about the space before the period.  We'll have
#      a way to fix that soon.

s = input('What is your name? ')
print('Hi', s, '.  It is a pleasure to meet you.')
print()


# Type-casting from string to integer.
#
# -- What happens if the user types a string that isn't an integer?
# -- What happens if you replace "int(s)" with just "s" and run the program? Why?

s = input('Please enter an integer: ')
number = int(s)

print('The square of', number, 'is', number * number)
print()
