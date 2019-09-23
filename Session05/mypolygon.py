import turtle
import math

brian = turtle.Turtle()

print(brian)

#brian.fd(100)
#brian.lt(90)

#brian.fd(100)
#brian.lt(90)

#brian.fd(100)
#brian.lt(90)

#brian.fd(100)
#brian.lt(90)

def square(t, length):
    for i in range(4):
        t.fd(100)
        t.lt(90)
#square(brian, 200)

#def polygon(t, length, n):
    #for i in range(n):
        #t.fd(length)
        #t.lt(360/n)
#polygon(brian, 100, 3)

def circle(t,r):
    circumference = 2 * math.pi * r
    n = 30
    length = circumference/n
    polygon (t, length, n)
#circle(brian,100)

#polygon(brian, length=100, n=8)

def arc(t, r, angle):
    """
    Draw an arc with radius, r, and angle (in degree)
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360/n
    polyline(t, n, length, angle)

#polygon(brian, 8, 100)
arc(brian, 100, 360)

turtle.mainloop()
