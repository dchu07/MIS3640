def three_consecutive_double_words(word):
    index = 0
    while index < len(word)-5:
        if word[index] == word[index+1] and word[index+2] == word[index+3] and word[index+4] == word[index+5]:
            return True
        index += 1
    return False

def find_three_consecutive_double_words():
    f = open("Session09/words.txt")
    count = 0
    for line in f:
        word = line.strip()
        if three_consecutive_double_words(word):
            print(word)
            count += 1
    return count

print(find_three_consecutive_double_words())

