   1: >>> name = 'Shaun'
   2:
>>> for letter in name:
...     print(letter)
...
   3:
>>> for i, letter in enumerate(name):
...     print(i, letter)
...
   4: >>> # print index only
   5:
>>> for i, _ in enumerate(name):
...     print(i)
...
   6:
>>> for i in range(len(name)):
...     print(i)
...
   7: >>> a = [True, True, False, True]
   8: >>> sum(a)
3
   9: >>> suspects = ["John", "Paul", "George", "Ringo"]
  10: >>> sorted(suspects)
['George', 'John', 'Paul', 'Ringo']
  11: >>> suspects
['John', 'Paul', 'George', 'Ringo']
  12: >>> suspects.sort()
  13: >>> suspects
['George', 'John', 'Paul', 'Ringo']
  14: >>> new_suspects = suspects.sort()
  15: >>> new_suspects
  16: >>> name = ['Emely', 'Krishna', 'Patrick']
  17: >>> grades =[90, 80, 65]
  18: >>> names = ['Emely', 'Krishna', 'Patrick']
  19:
>>> for i in range(3):
...     print(names[i], grades[i])
...
  20: >>> grades = dict()
  21: >>> type(grades)
dict
  22: >>> grades
{}
  23: >>> grades['Emely'] = 90
  24: >>> grades
{'Emely': 90}
  25: >>> grades = { 'Emely': 90, 'Krishna': 80, 'Patrick': 65}
  26: >>> grades
{'Emely': 90, 'Krishna': 80, 'Patrick': 65}
  27: >>> len(grades)
3
  28: >>> grades['Krishna']
80
  29:
>>> class_roster = ['Krishna',
...                 'Emely',
...                 'Demi',
...                 'Gregory',
...                 'Spencer',
...                 'Myat Shwe Yee',
...                 'Carmen',
...                 'Victoria',
...                 'Jinna',
...                 'Nico',
...                 'Meiling',
...                 'Jenny',
...                 'Xintong',
...                 'Shaun',
...                 'Brian',
...                 'David',
...                 'Patrick',
...                 'Shirley',
...                 'Arteen',
...                 'Julie']
...
  30: >>> grades={}
  31:
>>> for name in class_roster:
...     import random
...     grades[name] = random.randint(50, 100)
...
  32: >>> grades
{'Krishna': 92,
 'Emely': 63,
 'Demi': 97,
 'Gregory': 55,
 'Spencer': 61,
 'Myat Shwe Yee': 54,
 'Carmen': 62,
 'Victoria': 60,
 'Jinna': 85,
 'Nico': 64,
 'Meiling': 71,
 'Jenny': 97,
 'Xintong': 57,
 'Shaun': 84,
 'Brian': 54,
 'David': 53,
 'Patrick': 93,
 'Shirley': 51,
 'Arteen': 91,
 'Julie': 86}
  33: >>> grades['Zhi']
  34: >>> 'Zhi' in grades
False
  35: >>> 'Victoria'
'Victoria'
  36: >>> 'Victoria' in grades
True
  37: >>> 86 in grades
False
  38: >>> 86 in grades.values()
True
  39:
>>> for name, score in grades.items():
...     if score>80:
...         print(name, score)
...
  40:
>>> for name in grades.keys():
...     print(name)
...
  41:
>>> for grade in grades.values():
...     print(grade)
...
  42: >>> grades
{'Krishna': 92,
 'Emely': 63,
 'Demi': 97,
 'Gregory': 55,
 'Spencer': 61,
 'Myat Shwe Yee': 54,
 'Carmen': 62,
 'Victoria': 60,
 'Jinna': 85,
 'Nico': 64,
 'Meiling': 71,
 'Jenny': 97,
 'Xintong': 57,
 'Shaun': 84,
 'Brian': 54,
 'David': 53,
 'Patrick': 93,
 'Shirley': 51,
 'Arteen': 91,
 'Julie': 86}
  43: >>> grades.get('Spencer', 0)
61
  44: >>> grades.get('Zhi', 0)
0
  45: >>> grades['Spencer']
61
  46: >>> grades['Zhi']