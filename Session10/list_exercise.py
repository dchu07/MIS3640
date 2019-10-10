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
        sum = 0
        for i in number:
            sum += i
        total += sum
    return total

# t = [[1, 2], [3], [4, 5, 6]]
# nested_sum(t)


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    total = [t[0]]
    start_adding = 1
    for number in range(len(t)-1):
        total.append(sum(t[:start_adding + 1]))
        start_adding += 1
    return total

# t = [1, 2, 3]
# print(cumsum(t))


def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    new_list = t[1:-1]
    return new_list

# t = [1, 2, 3, 4]
# middle(t)


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
    return t

# t = [1, 2, 3, 4]
# chop(t)


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
    if t == sorted(t):
        return True
    return False

# print(is_sorted([1, 2, 2]))


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
    for i in word2:
        if i not in word1:
            return False
    return True



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
    i = 0
    while i < len(s)-1:
        if s[i] in s[i+1:]:
            return True
        i += 1
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
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            return True
        i += 1
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

    print(has_adjacent_duplicates('cba'))
    print(has_adjacent_duplicates('abca'))
    print(has_adjacent_duplicates('abbc'))


if __name__ == "__main__":
    main()