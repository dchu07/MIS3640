#Question 2
#Write a program, fibonacci.py to compute the Fibonacci number of an integer , n.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Please enter a number to find its fibonacci: "))
if n < 0:
    print("Fibonacci does not exist for negative numbers.")
else:
    print("The fibonacci of", n, "is: ", fibonacci(n))
