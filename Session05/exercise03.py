#Session05 Exercise03
print('Session05 Exercise03:')

import turtle 
import math 

hello = turtle.Turtle()
print(hello)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    circum = 2 * math.pi * r 
    n = 100
    length = circum / n 
    polygon (t, length, n)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1 
    step_length = arc_length / n
    step_angle = angle / n 
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
def move(t, x, y):
    t.pu()
    t.setpos(x,y)
    t.pd()

#First Shape
#circle(hello,100)
#hello.left(60)
#arc(hello,100,120)
#hello.left(120)
#arc(hello,100,120)
#hello.left(120)
#arc(hello,100,120)

#2nd part
#move(hello,0,200)
# hello.right(60)
# arc(hello,100,120)
# hello.left(120)
# arc(hello,100,120)
# hello.left(120)
# arc(hello,100,120)


#2nd Shape
hello.pensize(3)
circle(hello, 100)
move(hello, 0, 100)
arc(hello, 50, 180)
move(hello,0,100)
arc(hello, 50, 180)
move(hello,3,28)
circle(hello,20)
move(hello, 3, 128)
circle(hello, 20)

#3rd Shape
#triangles
# circle(hello,100)
# move(hello,0,100)
# hello.lt(60)
# hello.fd(100)
# for i in range (2):
#     hello.lt(120)
#     hello.fd(100)
# hello.fd(100)
# for i in range (2):
#     hello.rt(120)
#     hello.fd(100)

# hello.rt(90)
# hello.fd(100)
# for i in range (2):
#     hello.lt(120)
#     hello.fd(100)
# hello.fd(100)
# for i in range (2):
#     hello.rt(120)
#     hello.fd(100)

# #circles
# move(hello, -14, 135)
# circle(hello,27.5)
# move(hello, -14, 18)
# circle(hello,27.5)
# move(hello,45, 76)
# circle(hello,27.5)
# move(hello, -72, 76)
# circle(hello,27.5)

turtle.mainloop()