#defining a function
def print_lyrics():
    print("Hey Jude, Don't make it bad.")
    print("Take a sad song and make it better.")

#print_lyrics()

#print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print("Na - na - na - na - na, na - na - na - na")
    print_lyrics()

#repeat_lyrics()

def print_twice(whatever_name):
    print(whatever_name)
    print(whatever_name)

#print_twice() <-- this is an error, must be something inside the ()
#print_twice("Brian")
#print_twice("Hey, Jude")

#my_name = "Demi"
#print_twice(my_name)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

#line1 = 'Bing tiddle '
#line2 = 'tiddle bang.'
#cat_twice(line1, line2)

#print(cat) <-- cat only exists in the function

#def give_me_a_break():
    #msg = "break"
    #return msg

#print(give_me_a_break())

def give_me_a_break():
    str1 = 'break'
    return str1
    #print('another break') <-- everything after return will no be executed
    
#rint(give_me_a_break())

from my_abs import my_abs
print(my_abs(-5))