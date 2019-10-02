# team = "New England Patriots"
# letter = team[0]
# print(letter)

# print(team[1])

# print(team[1.5])

# print(len(team))
# print(team[-1])
# print(team[-20])

# index = 0
# while index < len(team):
#     letter = team[index]
#     print(letter)
#     index +=1 

# for letter in team:
#     print(letter)

# prefixes = "JKLMNOPQ"
# suffix = "ack"

# for letter in prefixes:
#     if letter == "O" or letter == "Q":
#         print(letter + "u" + suffix)
#     else:
#         print (letter + suffix)

team = "New England Patriots"
# print(team[0:11])
# print(team[:11])

# print(team[12:20])
# print(team[12:])

# slice
# print(team[::2])

#team[12:20] = "Seahawks"

new_team = team[:12] + "Giants"
# print(new_team)

# def find(word, letter):
#     index = 0
#     while index < letter(word):
#         if word[index] == letter:
#             return index
#         index += 1
#     return -1

def count(s, letter):
    counter = 0
    for c in s:
        if c.lower() == letter:
            counter += 1
    return counter

print(count(team,"a"))
print(count(team,"e"))