def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    print('Current a, b:', a, b) #for testing
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


if __name__ == "__main__":
    #print(gcdRecur(2, 12))
    #print(gcdRecur(6, 12))
    print(gcdRecur(9, 12))
    #print(gcdRecur(17, 12))