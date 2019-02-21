'''function.py

   Blake Howald 9/19/17, modified for Python 3 from original by Jeff Ondich, 25 September 2009

   A very brief example of how functions interact with
   their callers via parameters and return values.

   Before you run this program, try to predict exactly
   what output will appear, and in what order.  You are
   trying to trace the movement of data throughout the
   program, and make sure you understand what happens
   when.  This simple program is very important for you
   to understand.  If you have figured it out, the rest
   of the term will be a lot easier than if you haven't.
'''

def f(n):
    print(n)
    result = 3 * n + 4
    return result

def g(n):
    print(n)
    result = 2 * n - 3
    return result 

number = 5
print('number = ', number)
print()

print('Experiment #1')
answer = f(number)
print('f(number) =', answer)
print()

print('Experiment #2')
answer = g(number)
print('g(number) =', answer)
print()

print('Experiment #3')
answer = f(g(number))
print('f(g(number)) =', answer)
print()

