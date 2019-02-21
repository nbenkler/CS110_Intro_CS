# msdie.py
#    Class definition for an n-sided die.

from random import randrange

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value  

def main():

	die1=MSDie(12)
	print(die1.getValue())
	for i in range (10):
		die1.roll()
		print(die1.getValue())

main()