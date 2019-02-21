'''graphics3.py

   Started in Pascal by Jeff Ondich on 1/25/95
   Ported to C++, Java, and Python
   Last modified 4/14/09
   
   Modified for Python 3 compatibility 1/29/18 by Blake Howald

   1. Try it.

   2. How can you slow down or speed up the motion of the ball?

   3. The sleep function seems to have a minimum resolution--for
      example, I don't see a difference between the speed at 0.01 and
      and 0.005.  Is there something you can change in the step()
      method to speed up the animation?

   4. Try to get the ball to bounce from side to side instead
      of up and down.

   5. Can you get the colors to change gradually from red to blue
      and back instead of abruptly?
'''

import time
from graphics import *

class BouncingBall:
    def __init__(self, x, y, radius, window):
        self.window = window
        self.goingDown = True
        self.downColor = color_rgb(255, 0, 0)
        self.upColor = color_rgb(0, 255, 0)
        self.circle = Circle(Point(x, y), radius)
        self.circle.setFill(self.downColor)
        self.circle.draw(window)

    def step(self):
        windowHeight = self.window.getHeight()
        windowWidth = self.window.getWidth()
        x = self.circle.getCenter().getX()
        y = self.circle.getCenter().getY()

        if self.goingDown:
            dy = 40
        else:
            dy = -40

        if y + dy >= windowHeight - self.circle.getRadius():
            self.goingDown = False
        elif y + dy <= self.circle.getRadius():
            self.goingDown = True

        if self.goingDown:
            self.circle.setFill(self.downColor)
        else:
            self.circle.setFill(self.upColor)

        self.circle.move(0, dy)


# First, create a window with a white background.
windowWidth = 650
windowHeight = 500
window = GraphWin('Bounce', windowWidth, windowHeight)
window.setBackground(color_rgb(255, 255, 255))

# Create a BouncingBall object with the specified position and size,
# and associate it with the window created above.
ball = BouncingBall(windowWidth / 2, 50, 50, window)

# Until the user kills the program with a Ctrl+C, move the ball
# one step, wait for a bit, move the ball another step, wait, etc.
print('Type Ctrl-C in the terminal window to make the animation stop.')
while True:
    ball.step()
    time.sleep(0.02)

