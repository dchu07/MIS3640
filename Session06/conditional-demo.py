# age = int(input('Please enter your age:'))

# print(f'Your age is {age}.')
# if age >= 18:
#     print('You are an adult.')
# elif age>=10:
#     print('You are a teenager.')
# else:
#     print('You are a kid.')

# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

# x = int(input('Please enter a number for x:'))
# y = int(input('Please enter a number for y:'))

# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')

def compare(a,b):
    if isinstance(a, str) or isinstance(b, str):
        print('string involved')
    else:
        if a > b:
            print('bigger')
        elif a == b:
            print('equal')
        else:
            print('smaller')

compare('brian', 42)
compare(41, 42)