import random
import math

# Taking Inputs
lower = int(input("Enter lower bound: "))

# Taking Inputs
upper = int(input("Enter upper bound: "))

# Generating random number between upper and lower bound
x = random.randint(lower, upper)
chance = round(math.log(upper - lower + 1, 2))
string1 = "\n\tYou've only "
string2 = " chances to guess the integer!\n"

message = f'{string1} {chance} {string2}'
print(message)

# Initializing the number of guesses
count = 0

# For calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # Taking guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ", count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If guessing it more than required guesses, show this output
if count > math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")

