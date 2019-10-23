#exercise 1
#1
def word_with_more_than_20_char():
    file = open("Session09/words.txt")
    for line in file:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))

word_with_more_than_20_char()
#2
def has_no_e(word):
    for letter in word:
        if letter.lower() == "e":
            return False
    return True
def percetange_has_no_e():
    file = open("Session09/words.txt")
    number_of_words = 0
    count = 0
    for line in file:
        number_of_words += 1
        word = line.strip()
        if has_no_e(word):
            count += 1
    return count/number_of_words
print('{:.2f}%.'.format(percetange_has_no_e()*100))
#3
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
def avoids_aeiou():
    file = open("Session09/words.txt")
    count = 0
    for line in file:
        word = line.strip()
        if avoids(word, 'aeiou'):
            count += 1
    return count
print(avoids_aeiou())
#4
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
def uses_planet():
    file = open("Session09/word.txt")
    for line in file:
        word = line.strip()
        if uses_only(word, "planet")
            return True
    return False

#exercise 2
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True
#1
def is_abecedarian_using_recursion(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_using_recursion(word[1:])
#2
def is_abecedarian_using_while(word):
    index = 0
    while index < len(word)-1:
        if word[index + 1] < word[index]:
            return False
        index += 1
    return True



            
