import random
print("I am thinking of a number between 1 and 20. What is it?")
print("You have 4 tries.")
correct_answer = random.randint(1, 20)
guess = 0
valid_responses = list(range(1,21))
tries = 0


while guess != correct_answer and tries != 4:

    try:
        guess = int(input("Guess:   "))
    except ValueError:
        print("Choose a number from 1 to 20.")
        continue
    if guess in valid_responses:
        tries += 1
        if guess > correct_answer:
            print("Your guess is too high.")
        elif guess < correct_answer:
            print("Your guess is too low.")
        elif guess == correct_answer:
            print("You got it!")
    else:
        print("Choose a number from 1 through 20.")
        continue

if tries >= 4 and guess != correct_answer:
    print("You lose.")

        


