#Question 1
def cost(item):
    price = 0
    for i in range(len(item)):
        p = int(ord(item[i]))-96
        price += p
    print(item, "$" + str(price))

def total(groceries):
    all = 0
    for i in range(len(groceries)):
        all += groceries[1]
        print(all)

cost("bananas")
cost("rice")
cost("paprika")
cost("potato chips")
print("------------------------")
total("bananas")
