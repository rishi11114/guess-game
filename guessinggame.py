import random

jackpot = random.randint(1, 100)
guess = int(input("enter  your guess = "))

counter = 1
while guess != jackpot:
    if guess < jackpot:
        print(" guess higher")
    else:
        print("guess lower")
    guess = int(input("enter ter your guess = "))
    counter += 1
    
print(" right answer")
print(" you attempted", counter, "attempts")
