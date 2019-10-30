from point1 import *
import copy
import math

class Circle:
    """Represents a circle.

    Attributes: center, radius
    """


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).

    point: Point object
    circle: Circle object
    """
    return (distance_between_points(point, circle.center) <= circle.radius)

# circle = Circle()
# circle.center = Point()
# circle.center.x = 5
# circle.center.y = 5
# circle.radius = 5
# boxcorner = Point()
# boxcorner.x = 3
# boxcorner.y = 3
# print(point_in_circle(boxcorner,circle))


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    if not point_in_circle(p, circle):
        return False
    p.x += rect.width
    if not point_in_circle(p, circle):
        return False
    p.y -= rect.height
    if not point_in_circle(p, cirlce):
        return False
    p.x -= rect.width
    if not point_in_circle(p ,circle):
        return False
    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    if point_in_circle(p, circle):
        return True
    p.x += rect.width
    if point_in_circle(p, circle):
        return True
    p.y -= rect.height
    if point_in_circle(p, cirlce):
        return True
    p.x -= rect.width
    if point_in_circle(p ,circle):
        return True
    return 
    

def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()