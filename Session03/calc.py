#Session02 Exercise01
print('Session02 Exercise01:')

# 1.1
a = 3
print('1.1')
print('Value:', a + 2)
print('Type: Integer')

# 1.2
#a = a + 1.0
#a
print('1.2')
print('Value:',a + 1.0)
print('Type: Float')

# 1.3
#a = 3
#b
print('1.3')
print('Value: No b')
print('Type: error')

# 1.4
#a = 3
#a == 5.0
#a 
print('1.4')
print('Value: False')
print('Type: Boolean')

# 1.5
#b = 10
#c = b > 9
#c 
print('1.5')
print('Value: True')
print('Type: Boolean')


#1.6
print('1.6')
print('Value:', 5/2 == 5/2.0)
print('Type: Boolean')

#Q2
print('#Q2')
print(3.0 - 1.0 != 5.0 - 3.0)
print(3 > 4 or (2 < 3 and 9 > 10))
print (a > 5 or 3 < 4 and 9 > 8)
print (not(4 > 3 and 100 > 6))

#Q3
print('#Q3')
import time
epoch = time.time()
#60*60*24 is the seconds in a day
days = epoch / (60 * 60 * 24)
hour = days % int(days) * 24
min  = hour % int(hour) * 60
sec  = min % int(min) * 60

print('Time: %d:%d:%d' % (hour,min,sec))
print('Days: %d' % (days))