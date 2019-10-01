import math

def mysqrt(a):
    x = a/2
    while True:
        y = (x + a/x) / 2 
        if y == x:
            return y
            break
        x = y

print(mysqrt(2))

def test_square_root(a):
    print(a)
    print(mysqrt(a))
    print(math.sqrt(a))
    print(abs(mysqrt(a) - math.sqrt(a)))

test_square_root(10)