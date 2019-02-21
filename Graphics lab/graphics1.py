'''graphics1.py

   Started in Pascal by Jeff Ondich on 1/25/95
   Ported to C++, Java, and Python
   Last modified 10/5/09
   
      Modified for Python 3 compatibility 1/29/18 by Blake Howald
  
   1. Run it, and read all the functions to see what they do.
  
   2. Try changing the parameters passed to sayHello(), sayHelloAgain(),
      drawSomeCircles().  How do the parameters affect the picture?
  
   3. Where is the origin (0,0) in the coordinate system of GraphWin?
      Are larger y values higher or lower on the screen?  Are larger
      x values further right or further left on the screen?  How can
      you tell?
'''

from graphics import *


def movePen(window, pen, dx, dy, color):
    '''Draws a line of the specified color from the Point
       pen to the Point (dx, dy) away from pen (where the
       variable names "dx" and "dy" are intended to evoke
       the "delta x" and "delta y" of science experiments).
       Once the line is drawn, movePen changes the value of
       pen to equal the line's destination endpoint.

       For example, if pen = Point(10, 20), dx = 50, and
       dy = 80, then movePen draws a line from Point(10,20)
       to Point(60, 100), and then sets pen equal to
       Point(60, 100) so further drawing can start from there.

       Note that since this function does not save the Line
       object it creates, there is no way to later un-draw
       the Line.'''
    endPoint = Point(pen.x + dx, pen.y + dy)
    line = Line(pen, endPoint)
    line.setOutline(color)
    line.draw(window)
    pen.x = endPoint.x
    pen.y = endPoint.y

def sayHello(window, startX, startY):
    lineColor = color_rgb(255, 0, 255)
    pen = Point(startX, startY)
    movePen(window, pen, 30, -80, lineColor)
    movePen(window, pen, -10, -20, lineColor)
    movePen(window, pen, 0, 100, lineColor)
    movePen(window, pen, 10, -30, lineColor)
    movePen(window, pen, 10, 0, lineColor)
    movePen(window, pen, 10, 30, lineColor)
    movePen(window, pen, 15, 0, lineColor)
    movePen(window, pen, 10, -30, lineColor)
    movePen(window, pen, 5, 20, lineColor)
    pen = Point(pen.x - 10, pen.y - 40)
    movePen(window, pen, 0, -10, lineColor)

def sayHelloAgain(window, x, y):
    textColor = color_rgb(255, 0, 0)
    text = Text(Point(x, y), 'Blake')
    text.setTextColor(textColor)
    text.setSize(24)
    text.draw(window)

def drawSomeCircles(window, y):
    circleColor = color_rgb(0, 0, 255)
    circle = Circle(Point(150, y), 50)
    circle.setOutline(circleColor)
    circle.draw(window)

    circle = Circle(Point(350, y), 50)
    circle.setFill(circleColor)
    circle.draw(window)


# All the functions are defined.  Now start doing stuff.

# Open the window
windowWidth = 600
windowHeight  = 500
window = GraphWin('Graphics demo', windowWidth, windowHeight)
backgroundColor = color_rgb(255, 255, 255)
window.setBackground(backgroundColor)

# Draw some things.
drawSomeCircles(window, 100)
sayHello(window, 100, windowHeight - 100)
sayHelloAgain(window, windowWidth - 250, windowHeight - 100)

# Wait for user input.
s = input('Hit Enter to quit')
