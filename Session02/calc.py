#Session02 Exercise01
print('Session02 Exercise01:')
#Q1
import math
r = 5 
v = 4/3*math.pi*(r**3)
print('The volume of sphere with a radius of 5 is {:0.2f}'.format(v))
#Q2
p = 24.95 #pirce per book
d = 0.60 #discount
s1 = 3 #shipping cost for first book
s2 = 0.75 #shipping cost for every book after the first
cost = p*d*60 + s1+(s2*59)
print('The total wholesale cost is {:0.2f}'.format(cost))
#Q3
current = (6*60+52)*60 #current time in seconds
easy = (8*60+15)*2 #easy pace in seconds (2 miles)
fast = (7*60+12)*3 #fast pace in seconds (3 miles)

finish_in_min = ((current + easy + fast)/60)
finish_hr_min = finish_in_min/60
minutes = finish_hr_min %1
min = minutes*60

finish_hr = (current + easy + fast)/(60*60)
print ('The time I get home for breakfast is %d:%d' % (finish_hr,min)) #how to display time
#Q4
original = 82
new = 89
increase = (new-original)/original
print('The percent increase {:.1%}'.format(increase))