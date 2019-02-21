'''lists.py

   Originally created by Jeff Ondich (2009), modified by Blake Howald (9/8/17)

   This sample program will introduce you to Python lists.
   Read the code, figure out what it does, and try to answer
   any questions in the comments below.
'''

# Creating and printing a list
# -- How would you print just the third item in this list?  (Go back
#       to strings1.py for a hint.)
# -- What happens if you try to print the 5th item in this list?

firstList = [27, 'fireman', 3.14, 'freddy']
print(firstList)
print()

# Concatenating lists
# -- What does using the + operator between lists do?
# -- Does concatenating lists modify the original lists?

secondList = ['red', 'blue', 'green']
thirdList = firstList + secondList
print('First list:', firstList)
print('Second list:', secondList)
print('Third list:', thirdList)
print()

# Iterating over a list's contents
#  Just as with the strings in strings2.py, there are two main ways
#  to iterate over the elements in a list.
# -- What happens if you change "item" to some other word everywher
#    "item" appears?  Do the loops still work?
# -- What happens if you change the word "in" to something else?
#    Does the first loop still work?
# -- Does TextWrangler give you any hints about which words you get
#    to change and which ones you don't?

print('Iterating over a list')
for item in firstList:
    print(item)
print()

print('Iterating again, but in a different way')
k = 0
while k < len(firstList):
    print(firstList[k])
    k = k + 1
print()

# A couple list operations.  Figure out what they're doing, and how
# append and extend differ.

theList = [4, 5, 6]
print('Before append:', theList)
theList.append(7)
print('After append:', theList)
print()

theList = [4, 5, 6]
otherList = [7, 8]
print('Before extend:', theList)
theList.extend(otherList)
print('After extend:', theList)

theList = [4, 5, 6]
otherList = [7, 8]
print('Before append:', theList)
theList.append(otherList)
print('After append:', theList)
print()


# Some questions for your amusement.
# -- Can a list contain a list as one of its elements?
# -- Does slicing work with lists?

