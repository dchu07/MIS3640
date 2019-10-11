def histogram(s):
    d = dict()
    for letter in s:
        # if letter not in d:
        #     d[letter] = 1
        # else:
        #     d[letter] += 1
        d[letter] = d.get(letter, 0) + 1
        # print(d)
    return d


h = histogram("bookkeeper")
print(h)