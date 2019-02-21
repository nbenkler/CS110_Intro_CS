'''strings2.py

   Originally created by Jeff Ondich (2009), modified by Blake Howald (9/8/17)

   This sample program will introduce you to "iteration" or
   "looping" over the characters in a string.
'''

s = 'I will see you again in 25 years'

# What happens here?
print('The first loop')
for ch in s:
    print(ch)
print()


# And here?
print('The second loop')
k = 0
while k < len(s):
    print(s[k])
    k = k + 1
print()

# Can you make sense of these structures?  
# What happens if you comment out k = k + 1?
# We'll discuss more next week 


