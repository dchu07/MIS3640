# fin = open("session09/words.txt")
# line = fin.readline()
# word = line.strip()
# print(word)

# for line in fin:
#     word = line.strip()
    # print(word)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open("Session09/words.txt")
    for line in f:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))

# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    for letter in word:
        if letter.lower() == "e":
            return False
    return True

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open("Session09/words.txt")
    count = 0
    num_of_words = 0
    for line in f:
        num_of_words += 1
        word = line.strip()
        if has_no_e(word):
            count += 1
    return count/num_of_words
            
# print('The percentage of the words with no "e" is {:.2f}%.'.format(find_words_no_e()*100))


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True

# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't vowel letters
    """
    f = open("Session09/words.txt")
    num_of_words_with_no_vowel = 0
    num_of_word = 0
    for line in f:
        num_of_word += 1
        word = line.strip()
        if avoids(word, "aeiou"):
            num_of_words_with_no_vowel +=1
    return num_of_words_with_no_vowel/num_of_word

# print('The percentage of the words with vowel letters is {:.2f}%.'.format(find_words_no_vowels()*100))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True

# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planet():
    f = open("Session09/words.txt")
    num_of_words_only_use_planet = 0
    for line in f:
        word = line.strip()
        if uses_only(word,"planet"):
            num_of_words_only_use_planet += 1
    return num_of_words_only_use_planet

# print('Number of words that use letters from "planet" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
        if letter not in word:
            return False
    return True
 
# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))
# print(uses_all('Babson', 'aeoiu'))
# print(uses_all('Babesonious', 'aeoiu'))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open("Session09/words.txt")
    count_num_of_word_with_vowels = 0
    for line in f:
        word = line.strip()
        if uses_all(word, "aeiou"):
            count_num_of_word_with_vowels += 1
    return count_num_of_word_with_vowels

# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = word[0]
    for letter in word:
        if letter < before:
            return False
        before = letter
    return True

# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words and the longest abecedarian word
    """
    f = open("Session09/words.txt")
    count_words_in_order = 0
    for line in f:
        word = line.strip()
        if is_abecedarian(word):
            count_words_in_order += 1
    return count_words_in_order

# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_using_recursion(word[1:])

# print(is_abecedarian_using_recursion('abs'))
# print(is_abecedarian_using_recursion('apps'))
# print(is_abecedarian_using_recursion('college'))    


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    index = 0
    while index < len(word)-1:
        if word[index + 1] < word[index]:
            return False
        index += 1
    return True

# print(is_abecedarian_using_while('abs'))
# print(is_abecedarian_using_while('apps'))
# print(is_abecedarian_using_while('college')) 