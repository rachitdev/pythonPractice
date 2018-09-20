import random

highest = 10
answer = random.randint(1, highest)
num_try = 1

print("Enter your guess number in between 1 and 10: ")
guess = int(input())

while guess != answer:
    if guess == 0:
        print("You chose to quit! Thanks for Playing! Game Over!")
        break
    if guess < answer:
        print("Please guess again with a higher quantity: ")
        guess = int(input())
        num_try += 1
        print("Number of tries in guessing the right answer: {}".format(num_try))
    elif guess > answer:
        print("Please guess again with a lower quantity: ")
        guess = int(input())
        num_try += 1
        print("Number of tries in guessing the right answer: {}".format(num_try))
    elif guess == answer:
        print("Smart Guess, You win!")
        num_try += 1
        print("Number of tries in guessing the right answer: {}".format(num_try))
