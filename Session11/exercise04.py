# Question 1
# Write a function that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to
# check whether a string is in the dictionary.
def reads_words():
    file = open("Session09/words.txt")
    word_dict = dict()
    for line in file:
        word = line.strip()
        word_dict[word] = word
    return word_dict

print(reads_words())

#Question 2
# Write a function named has_duplicates that takes a list as a parameter and returns
# True if there is any object that appears more than once in the list.
def has_duplicates(list):
    dictionary = {}
    for value in list:
        dictionary[value] = 1 + dictionary.get(value, 0)
        if dictionary[value] > 1:
            return True
    return False

list = [1, 2, 3, 4, 5, 6, 1, 6]
print(has_duplicates(list))
    
