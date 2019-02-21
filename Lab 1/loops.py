'''loops.py

      Blake Howald 9/19/17, modified for Python 3 from original by Jeff Ondich, 21 September 2009

   This sample program investigates several loop structures.
'''

# Since there are a lot of pieces to this program, you
# may want to use copy and paste to run just one piece
# at a time while you investigate each kind of loop
# structure.  That's up to you.

# The "for x in y" loop behaves differently depending on
# what type of object y refers to.  Here, for example, is
# a for-loop using a string for y.  When this loop runs,
# what kind of thing is x?

print('====== looping over a string ======')
y = 'Sally and Nick in the backyard'
for x in y:
    print(x)
print()

# Suppose y is a list.  Then what kind of thing is x during
# each iteration of the loop?

print ('====== looping over a list ======')
y = ['Sally', 'Nick', 'backyard']
for x in y:
    print(x)
print()

# Suppose y is an open file.  What is x then?

print ('====== looping over a file ======')
y = open('loops.py')
for x in y:
    print(x)
print()
y.close()

# Can you loop over an integer?  (Try doing y = 23 before
# for x in y, and see what happens.)

# You might not be able to loop over an integer (d'oh! I gave
# it away!), but you can loop over a "range" of integers.
# This is what your textbook calls a "definite" loop (see section
# 2.6).

print('====== looping over a range ======')
y = 7
for x in range(y):
    print(x)
print()

# Want to understand why looping over a range works? Try
# just doing:
#
#    print range(7)
#
# What kind of object is range(7)?


# Moving on.  Let's talk about while-loops.

# -- Run the loop below and see what happens.
# -- What happens if you remove the "k = k - 1" line?
# -- Can you make the loop count down by twos?
# -- Can you make the loop count up by threes from 0 to 999?

print('====== a while-loop counting down ======')
k = 10
while k > 0:
    print(k)
    k = k - 1
print('Boom.')
print()

# Here's another while-loop.  Compare it to the for x in y
# loop above where y was a string.

print('====== a while-loop and a string ======')
y = 'Sally again'
k = 0
while k < len(y):
    print(y[k])
    k = k + 1
print()

# while-loops can do a lot of things other than simple
# counting.  What does this loop do?

print('====== a more sophisticated while-loop and a string ======')
y = 'Nick again'
k = 0
s = ''
while k < len(y) and y[k].isalpha():
    s = s + y[k]
    k = k + 1
print('The resulting string is:', s)
print()


# Next: nested loops.  That is, loops inside loops.
# Try to predict what this loop will print.

print('====== nested loops, first example  ======')
for j in range(4):
    for k in range(3):
        print(j, k)
print()

# This one's trickier.  Can you predict it?  Can
# you explain why it does what it does?

print('====== nested loops, trickier ======')
for j in range(4):
    for k in range(j):
        print(j, k)
print()

