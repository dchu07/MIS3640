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
def read_file_to_list(path_to_file):
    """
    reads file of words, return a list of words
    """
    file = open(path_to_file)
    words = []
    for line in file:
        word = line.strip()
        words.append(word)
    return words

def list_to_dict(words):
    """
    converts a list of words to a dictionary and the dictionary should be like:
    {aedlts:["deltas", "desalt", "lasted", "salted", "slated", "staled"]}
    """
    d = {}
    for word in words:
        fingerprint = "".join(sorted(word))
        if fingerprint not in d:
            d[fingerprint] = [word]
        else:
            d[fingerprint].append(word)
    return d


def print_anagrams(word_dict, n_words_in_anagram=1):
    """
    prints all the anagrams with more than one word
    """
    for eachlist in word_dict.values():
        if len(eachlist) > n_words_in_anagram:
            print(eachlist)

def create_new_dict(old_dict):
    """
    create a new dictionary, key is number, values is the anagrams with the same number of words
    create an empty dictionary, d

    for each value (a word list) in the old dictionary,
	    get how many words there are in the list and assign to a temp variable, k
	    if first time we see k:
		    add k as key in d, value is a new list that contains the old word list
	    else:
		    append the old word list to d[k]
	    return new dictionary
    """
    d = {}
    for v in old_dict.values():
        k = len(v)
        if k not in d:
            d[k] = [v]
        else:
            d[k].append(v)
    return d

def print_anagram_this_way(word_dict):
    """
    words_dict is a dictionary with integer (key): list of word lists (value) pairs
    print the list of word lists in descending order of integers
    """
    for num in sorted(word_dict.keys(), reverse = True)[:2]:
        print(num)
        print(word_dict[num])

def main():
    path_to_words_file = "Session13/words.txt"
    words_list = read_file_to_list(path_to_words_file)
    anagrams = list_to_dict(words_list)
    # print_anagrams(anagrams, n_words_in_anagram=3)

    #create a new dictionary, key is number, values is the anagrams with the same number of words
    new_dict = create_new_dict(anagrams)
    #then print the dictionary
    print_anagram_this_way(new_dict)

    # words_list = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'resmelts', 'smelters', 'termless', 'brian]
    # anagrams = list_to_dict(words_list)
    # print(anagrams)

if __name__ == "__main__":
    main()

# def find_anagrams():
# """Write a program that reads a word list from a file and prints all the sets of words that are anagrams."""
#     file = open("Session13/words.txt")
#     result = dict()
#     for line in file:        
#         word = line.strip()
#         sets = ''.join(sorted(word))
#         result.append(sets)
#     return result
# find_anagrams()

#2.3
# def sort_anagrams(anagrams):
#     """Modify the previous program so that it prints the longest list of anagrams first,
#     followed by the second longest, and so on."""
#     anagrams_lists = []
#     for i in anagrams:
#         anagrams_lists.append(anagrams[i])
#     anagrams_lists.sort(key=len, reverse=True)
#     return anagrams_lists

# anagrams = ('deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled')
# sort_anagrams(anagrams)
