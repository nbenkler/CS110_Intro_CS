'''graphics0.py

   Developed originally in Pascal by Jeff Ondich on 1/25/95
   Ported to C++, Java, and Python
   Last modified 4/14/09
   
   Modified for Python 3 compatibility 1/29/18 by Blake Howald
  
   This program opens a graphics window, fills it with a black
   background, and draws a red circle in the center.
  
   Try doing these things:
  
   0. Run the program as it is.  You'll need a copy of John
      Zelle's graphics.py in your working directory.
   1. Read the whole program to find out how it works.
   2. What happens if you remove the "s = raw_input('')" at the
      end of the main program?
   3. Modify the code to draw a tall and skinny graphics
      window.  Where does the circle get drawn when you
      run your new version of the program?  Why?
   4. Change the background color.  Can you make it white?
   5. Make the circle green.
'''
   

from graphics import *

# Define some values that we will use later.  It is handy
# to define these quantities together here at the top, because
# that makes it easy to modify them later.
windowHeight = 600
windowWidth = 400
windowTitle = 'Circle Demo'
radius = 100

# Define some colors.  To do color graphics, you specify
# colors via red, green, and blue values.  A red value of
# 0 means no red at all, while a red value of 255 means
# as much red as possible.  For example, color_rgb(255, 0, 255)
# is a bright purple, while color_rgb(150, 0, 150) is a
# darker purple.
backgroundColor = color_rgb(255, 255, 255)
circleColor = color_rgb(0, 255, 0)

# Open a window with the specified title, width, and height.
window = GraphWin(windowTitle, windowWidth, windowHeight)
window.setBackground(backgroundColor)

# Create and draw a circle.
center = Point(windowWidth / 2, windowHeight / 2)
circle = Circle(center, radius)
circle.setFill(circleColor)
circle.draw(window)

# Wait for user input.
response = input('Hit Enter to quit')

