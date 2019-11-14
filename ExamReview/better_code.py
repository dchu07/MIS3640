# def f1(a=[]):
#     a.append('Shaun')
#     print(a)

# f1()
# f1()
# f1()

# def f2(a=None):
#     # if a == None:
#     if a is None:
#         a = []
#     a.append('Brian')
#     print(a)

# f2()
# f2()
# f2()

# from math import log10
# a = log10(100)
# print(a)

# log10 = log10(100) #naming conflict

# print(log10(1000))

# num1 = 10_000_000
# num2 = 100_000_000

# print(num1)
# sum = num1 + num2
# print(f'{sum:,}')


"""
content
"""
# f = open('ExamReview/t.txt')
# content = f.read()
# print(content)
# f.close()

# print(len(content.split()))


"""
Enumerate
"""
# names = ['Victoria', 'Carmen', 'Myat', 'Nico']
# i = 0
# for name in names:
#     print(i,name)
#     i += 1

#better code
# for i, name in enumerate(names, start = 1):
#     print(i, name)


names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne', 'Brian']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

# for i,name in enumerate(names):
#     hero = heroes[i]
#     print(f'{name} is actually {hero}.')

#better code
for name, hero, u in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {u}.')

