import random

count = 0
gen_number = random.randrange(1, 10)

while True:
    guess = input("Guess the number... ")
    if guess == 'exit':
        print("You tried %d times." % count)
        break

    if int(guess) == gen_number:
        print("You guessed it! You tried %d times." % count)
        break
    elif int(guess) > gen_number:
        count += 1
        print("Too high!")
    elif int(guess) < gen_number:
        count += 1
        print("Too low!")
