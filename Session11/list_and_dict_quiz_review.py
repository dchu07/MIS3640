#lists review
def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
    t: list of list of numbers
    returns: number
    Expected output:
    >>> t = [[1, 2], [3], [4, 5, 6]]
    >>> nested_sum(t)
    21
    """
    total = 0
    for number in t:
        total += sum(number)
    return total


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    list = []
    total = 0
    for number in t:
        total += number
        list.append(total)
    return list


def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    return t[1:-1]


def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    """
    del t[0]
    del t[-1]


def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    return t == sorted(t)


def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    Two words are anagrams if you can rearrange the letters from one to 
    spell the other.
    word1: string or list
    word2: string or list
    returns: boolean
    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """
    return sorted(word1) == sorted(word2)


def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    count = 0
    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            count += 1
            if count == 2:
                return True
    return False
    
# print(has_duplicates('cba'))
# print(has_duplicates('abba'))

def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.
    s: string or list
    returns: bool
    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            return True
    return False


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == "__main__":
    main()

#dictionaries review
#Rewrite function histrogram using get. You should be able to eliminate the if statement
def historgram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

print(historgram("Bookkeeper"))


#Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are.
#Then you can use the in operator as a fast way to check whether a string is in the dictionary.
def words():
    file = open("Session09/words.txt")
    word_dict = dict()
    for line in file:
        word = line.script()
        word_dict[word] = word
    return word_dict


#Write a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than
#once in the list.
def has_duplicates_dict(list):
    dictionary = {}
    for value in list:
        dictionary[value] = 1 + dictionary.get(value, 0)
        if dictionary[value] > 1:
            return True
    return False

#testing code
