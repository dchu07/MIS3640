#Question 3
#The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder.
#For example,
    #gcd(2, 12) = 2
    #gcd(6, 12) = 6
    #gcd(9, 12) = 3
    #gcd(17, 12) = 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
print ("The greatest common divisor of",a, "and",b, "is:",gcd(a,b)) 