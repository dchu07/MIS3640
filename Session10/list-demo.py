a = [10, 20, 30, 40]
type(a)
len(a)
b = ['spam', 2.0, 5, [10,20]]
len(b)

b[3][0]
b[3] = [10]
# replaces [10,20] with just [10]

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# numbers = [42, 123]
# empty = []
# print(AFC_east, numbers, empty)

# AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
# print('Buffalo Bills' in AFC_east)

#exercise 1
L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', ['Ruby','On Rail'], 'PHP'], ['Adam', 'Bart', 'Lisa'] ]
#Apple
L[0][0]
#Lisa
L[2][2]
L[-1][2]
#Rail
L[1][2][1]
#   <- Space
L[1][2][1][2]

# name = "Brian"
# for whatever in name:
#     print(whatever)

# for team in AFC_east:
#     for letter in team:
#         print(letter)


# numbers = [2, 0, 1, 6, 9]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
# print(numbers)

# numbers = [2, 0, 1, 6, 9]
# for number in numbers:
#     number = number * 2
# print(numbers)

# my_list = ['spam', 1, ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Giants'], [1, 2, 3]]
# print(len(my_list))


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
#combinin two list into one list

#prints 0 x4
# [0] * 4

#prints a new lists with x3
# ['Tom Brady', 'Bill Belichick']*3

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[::2])
# #or
# print(t[0:6:2])
# print(t[::-2])
# t[1:3] = ['x', 'y']
# print(t)

#mapping
def capitalize_all(t):
    result = []
    for word in t:
        result.append(word.capitalize())
    return result

names = ['nico', 'myat', 'carmen']
# print(capitalize_all(names))

#reducing
t = [1, 2, 3]
# print(sum(t))

#filtering
names = ['Jinna','SHAUN', 'julie']
def only_upper(t):
    result = []
    for word in t:
        if word.isupper():
            result.append(word)
    return result

print(only_upper(names))