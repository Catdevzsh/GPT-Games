## write a guessing game
print("Guess a number between 1 and 10")
guess = int(input())
# make a algrothim that will guess the number
print("Enter the number you want the computer to guess")
number = int(input())
## make a random number generator
import random
random_number = random.randint(1,10)

### give the user 5 tries to guess the number
print("You have 5 tries to guess the number")
guess = int(input())
if guess == number:
    print("You guessed the number")
else:
    print("You did not guess the number")
    print("You have 4 tries left")
    guess = int(input())
    if guess == number:
        print("You guessed the number")
    else:
        print("You did not guess the number")
        print("You have 3 tries left")
        guess = int(input())
        if guess == number:
            print("You guessed the number")
        else:
            print("You did not guess the number")
            print("You have 2 tries left")
            guess = int(input())
            if guess == number:
                print("You guessed the number")
            else:
                print("You did not guess the number")
                print("You have 1 tries left")
                guess = int(input())
                if guess == number:
                    print("You guessed the number")
                else:
                    print("You did not guess the number")
                    print("You have 0 tries left")
                    print("Game Over")
                    print("The number was", number)
                    print("The computer guessed", random_number)
# 