'''strings3.py

   Blake Howald 9/19/17, modified from original by Jeff Ondich, 2 April 2009

   This sample program will introduce you to some standard string
   operations.  See http://docs.python.org/library/stdtypes.html#id4
   for documentation on these operations and many more.
'''

# Using the "replace" method.
#
# -- Go to the link shown above, and scroll down to the paragraph
#     about "str.replace".  Does the description of "replace" in
#     this documentation describe what you observe when you run the
#     the code below?  (It should, but you never know...)
# -- Do the replace operations below modify the string s, or just t?
#     Why does one change, but not the other?
# -- In the second replace operation, what would happen if we did
#     t = s.replace('cranky', 'content') instead of what's there?

s = 'The apple and the banana are cranky.'
t = s.replace('apple', 'peach')
t = t.replace('cranky', 'rotten')
print('Original:', s)
print('Modified:', t)
print()


# Using the "find" method.
#
# -- Read about str.find in the Python string documentation (same
#     link as above).  Try to predict what the following code will
#     print before you run it.

s = 'The apple and the other apple are rotten.'
print(s.find('apple'))
print(s.find('rotten'))
print(s.rfind('apple'))

if s.find('apple') >= 0:
    print('There is a apple here.')
else:
    print('No apple.')

if s.find('rotten') >= 0:
    print('There is something rotten here.')
else:
    print('There is nothing rotten here.')

print()


# Exploring other methods.
#
# -- Take a look at the documentation for str.lower, str.upper,
#      str.strip, str.isdigit, and str.isalpha.  Create some
#      little tests for these operations to see whether they
#      work as you expect them to.  For example...

s = '12345'
if s.isdigit():
    print(s, 'is entirely composed of digits')
else:
    print(s, 'contains something that is not a digit')
print()

