import random


random_digit = str(random.randint(1000, 9999))
guess_counter = 0

while True:

    guess = input("Enter a 4 digit number: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Enter a 4 digit number.")
        continue

    cows = 0
    bulls = 0

    if guess == random_digit:
        print(f"Congratulations! You've guessed the number {random_digit} in {guess_counter + 1} attempts.")
        break

    for digit in range(len(guess)):
        if guess[digit] == random_digit[digit]:
            cows += 1
        elif guess[digit] in random_digit and guess[digit] != random_digit[digit]:
            bulls += 1
    guess_counter += 1

    print(f"{cows} cows, {bulls} bulls.")
