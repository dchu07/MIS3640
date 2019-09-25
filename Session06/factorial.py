#Question 1
#Write a program, factorial.py to compute a factorial of an integer, n.
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

n = int(input("Please enter a number to find its factorial: "))
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", n, "is: ", factorial(n))

