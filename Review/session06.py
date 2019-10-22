# age = 20
# if age >= 18:
#     print('Your age is', age)
#     print('adult')

#exercise 1
# weight = int(input("Please enter your weight in pounds: "))
# height = int(input("Please enter your height in inches: "))
# bmi = 703 * (weight/(height**2))
# if bmi <= 18.5:
#     print(f"Your BMI is {bmi} and you are underweight.")
# elif 18.5 <= bmi <= 24.9:
#     print(f"Your BMI is {bmi} and you are normal.")
# elif 25 <= bmi <= 29.9:
#     print(f"Your BMI is {bmi} and you are overweight.")
# elif bmi >= 30:
#     print(f"Your BMI is {bmi} and you are obese.")

#exercise 2
def compare(varA, varB):
    if isinstance(varA, str) or isinstance(varB, str):
        print("string involved")
    else:
        if varA > varB:
            print("bigger")
        elif varA == varB:
            print("equal")
        else:
            print("smaller")