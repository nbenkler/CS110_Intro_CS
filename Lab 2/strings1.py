'''strings1.py

   Originally created by Jeff Ondich (2009), modified by Blake Howald (9/8/17)

   This sample program will introduce you to string indexes
   and slicing.
'''

# Indexes (or indices, if you prefer the fancy plural).  You can get
# at the individual characters in a string via their numerical
# position in the string using the square bracket notation as
# shown below.  The numerical position of a character is
# called its "index".
#
# -- What is the index of the first character in a string?
# -- What happens if you access a negative index of a string?
# -- What happens if you try to access a really big index (e.g. s[100])?
# -- What do you think: should we say "indexes" or "indices"?  I am
#      ambivalent on the question.

s = 'the cow jumped over the moon'
print('s =', s)
print('len(s) =', len(s))
print('s[0] =', s[0])
print('s[1] =', s[1])
print('s[2] =', s[2])
print('s[-1] =', s[-1])
print('s[-2] =', s[-2])
print('s[-3] =', s[-3])
print() 


# Slices.
#
# -- What slice would give you the string 'jumped' (there are four possible answers here)?
# -- How would you print the first 6 characters of the string?
# -- How would you print the last 8 characters of the string?

print('s[0:3] =', s[0:3])
print('s[2:5] =', s[2:5])
print('s[2:] =', s[2:])
print('s[:2] =', s[:2])
print('s[2:-2] =', s[2:-2])
print()


