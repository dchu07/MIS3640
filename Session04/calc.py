#Session04 Exercise01
print('Session04 Exercise01:')

from math import sqrt

a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))
def quadratic(a,b,c):
    formula = b**2 -(4*a*c)
    if formula >= 0:
        return ("x= ",(-b + sqrt(formula))/(2*a), "x= ",(-b - sqrt(formula))/(2*a))
    if formula < 0:
        return ("x= ",-b/(2*a),"+",sqrt(formula*(-1))/(2*a),"i" 
                "x= ",-b/(2*a),"-",sqrt(formula*(-1))/(2*a),"i")

print(quadratic(a,b,c))
