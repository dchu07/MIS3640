varA = int(input('Please enter your weight in lbs.:'))
varB = int(input('Please enter you height in in.:'))

bmi = (varA/varB**2)*703

if bmi <= 18.5:
    print('You are underweight')
elif 18.8 <= bmi <= 24.9:
    print('Your weight is normal')
elif 25 <= bmi <= 29.9:
    print('You are overweight')
else:
    print('You are obese')
    
print(bmi)