#Question 1
Total = 0
words = ["bananas", "rice", "paprika", "potato chips"]

def cost(item): 
    price = 0
    for i in item:
        price += int(ord(i))-96
    return price

def total_price(words):
    total = 0 
    longest = 0
    for item in words:
        if len(item) > longest:
            longest = len(item)
    longest += 10
    for item in words:
        print('%-*s $%s' % (longest, item, (cost(item))))
        total += cost(item)
    print('-'*(longest*2))
    print('%-*s $%s' % (longest, 'Total ',(total)))
total_price(words)