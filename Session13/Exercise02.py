#2.1
def find_frequency(string):
    d = dict()
    for i in string:
        d[i] = d.get(i, 0) + 1
    return d

def most_frequent(word):
    dictionary = find_frequency(word)
    result = []
    for letter in dictionary:
        result.append((dictionary[letter], letter))
    result.sort(reverse=True)
    return result

# a = "aaabbcdeefffgggg"
# print(most_frequent(a))

#2.2
def find_anagrams():
"""Write a program that reads a word list from a file and prints all the sets of words that are anagrams."""
    file = open("Session13/words.txt")
    result = dict()
    for line in file:        
        word = line.split()
        sets = ''.join(sorted(word))
        result.append(sets)
    return result

find_anagrams()

#2.3
def sort_anagrams(anagrams):
    """Modify the previous program so that it prints the longest list of anagrams first,
    followed by the second longest, and so on."""
    anagrams_lists = []
    for i in anagrams:
        anagrams_lists.append(anagrams[i])
    anagrams_lists.sort(key=len, reverse=True)
    return anagrams_lists

anagrams = ('deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled')
sort_anagrams(anagrams)
