'''graphics2.py

   Started in Pascal by Jeff Ondich on 1/25/95
   Ported to C++, Java, and Python
   Last modified 1/19/07
   
      Modified for Python 3 compatibility 1/29/18 by Blake Howald
   
   1. Try it.

   2. Identify which corner of the polygon has which coordinates
      as listed in the source code.

   3. Redesign the polygon to be a triangle or a rectangle.
      Can you do a regular hexagon?

   4. What is the default background color of a GraphWin object?
'''

from graphics import *

window = GraphWin('Polygon demo', 600, 500)

polygon = Polygon(Point(200, 100),
                  Point(400, 100),
                  Point(500, 200),
                  Point(400, 300),
                  Point(200, 200))

polygonColor = color_rgb(255, 0, 0)
polygon.setOutline(polygonColor)
polygon.draw(window)


s = input('Hit Enter to quit')

