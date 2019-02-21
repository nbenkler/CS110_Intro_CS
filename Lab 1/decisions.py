'''decisions.py
   Originally created by Jeff Ondich (2009), modified for Python 3 by Blake Howald (9/8/17)

1. Read through this program and predict its behavior.
Run it several times with varying input.  Try to get all
the different output messages at one time or another.

2. What does "==" mean?  Do you have any idea why Python
doesn't just use "=" in this context?

3. What does "!=" mean?

4. One message asks "What do I know about that first number?"
If that message appears, what _do_ you know about the first
number?

5. Try replacing "and" with "or" in the code for the third
message.  How does this affect the program's behavior?

6. Try changing the indentations of various lines of code.
When do you get error messages, and why?  When do you get
no errors, but changed program behavior?  As you learn
more about Python, pay close attention to indentation and
its meaning in various contexts.
'''

a = eval(input('Integer, please: '))
b = eval(input('Another integer, please: '))
print()
	
# First message.
if a > b:
    print('That first number is big!')
else:
    print('Gosh, what a small first number.')

# Second message.	
if a < 0:
    print('Oooh...')
    print('The first number is also negative.')
else:
    if a == 0:
        print('The first is 0, my favorite number.')
    else:
        print('What do I know about that first number?')

# Third and fourth messages, maybe.
if a == 0 and b == 0:
    print('Pure Nothingness.  Cool.')
	
if b != 7:
    print('I wish the second number were 7.')

