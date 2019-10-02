def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

'''
If the word(string s) starts with a lowercase letter it will return True, or else if it starts with a uppercase letter
it will return False. Even if the word contains any uppercase letters but does not start with with one, it will stil
return True. (ONLY when it starts with an uppercase letter will it return False.)
'''
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

'''
This function will always return True, as this tests whether or not the string 'c' is lowercase regardless of what string
we input
'''

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

'''
If the word(string s) ends with a lowercase letter it will return True, or else if it ends with a uppercase letter
it will return False. Even if the word contains any uppercase letters but does not end with with one, it will stil
return True. (ONLY when it ends with an uppercase letter will it return False.)
'''

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

'''
If all letters in the string is uppercase then it would return False, or else a string with a mixture of lowercase and
uppercase letters or even just lowercase letters would return True.
'''

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

'''
If all letters in the string is lowercase then it would return True, or else containing any uppercase letters would
return False.
'''