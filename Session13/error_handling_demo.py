# try:
#     number = int(input("Please enter a number:"))
#     result = 2019 / number
#     print(result)
# except ZeroDivisionError as e:
#     print("Something is wrong: ", e)

# print("After something is wrong, we still can get here")

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

name_dict = {"Shaun": 90, "Brian": 80, "Victoria": 85}
try:
    print(reverse_lookup(d=name_dict, v=100))
except LookupError as e:
    print("There is no such value.")