#Session04 Exercise01
print('Session04 Exercise01:')

import math

def quadratic(a,b,c):
    try:
        x = (-b+(b**2-4*a*c)**(1/2))/(2*a)
        x2 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
        print(f"The value of x are: {x:.2f} and {x2:.2f}")
    except TypeError:
        print("Oops something is wrong")

quadratic(1,-5,"b")
