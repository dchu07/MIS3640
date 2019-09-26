import random

name = input("Hello! What is your name?")
trials = 1
cpu = random.randint(1,20)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
while trials <7:
    n = int(input("Take a guess."))
    if n < cpu:
        print("Your guess is too low")
        trials += 1
    elif n == cpu:
        print(f"Good Job, {name}! You guessed my number in {trials} guesses!")
        break
    else:
        print("Your guess is too high")
        trials += 1

    