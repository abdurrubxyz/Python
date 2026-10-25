import random

number = random.randint(1,30)
guess = int(input("Enter Your Guessing Number. Its less than 30 : "))

while number != guess:
    if guess > number:
        print("Your guess is higher")
    else:
        print("Your gues is lower")
    guess = int(input("Guess again : "))

print("You won")