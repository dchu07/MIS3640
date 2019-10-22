#numbers
# import math
# print(math.pi)
# print(math.sqrt(85))

# import random
# print(random.random())
# print(random.choice([1,2,3,4]))

# print('I\'m \"ok\".')  # Use escape character \
# print('\\\t\\') # t = tab
# print('\\\n\\') # n = new line
# print('''line1
# ... line2
# ... line3''')
# ... to display multiple line

# import random
# age = random.choice([5,10,20,30,40,50])
# print(age)
# if age >= 21:
#     print('Yes, you can.')
# else:
#     print('Sorry.')

#exercise 1
#1
a = 3
result = a + 3
print(result)
print(type(result))

#exercise 2
print(3.0 - 1.0 != 5.0 - 3.0)

#exercise 3
import time
current = time.time()
second = current % 60
minutes = (current // 60) % 60
hours = (current // 60) // 60 % 24
days = current // 60 // 60 // 24

print(f"Current time: {int(days):d} days, {int(hours):d} hours, {int(minutes):d} minutes and {second:.2f} seconds from Epoch.")