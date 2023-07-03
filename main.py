import random
MIN_NUMBER = 1
MAX_NUMBER = 100


def hidden_number():
    goal = random.randint(MIN_NUMBER, MAX_NUMBER)
    return goal


def main():
    goal_number = hidden_number()
    guess = input(f"Pick a number between {MIN_NUMBER}-{MAX_NUMBER}!")
    while guess != goal_number:
        if guess.isdigit():
            guess = int(guess)
            if guess == goal_number:
                print(f"Congratulations! The hidden number was {goal_number}")
            else:
                if guess > goal_number:
                    print("Your number was greater than the hidden number.")
                    guess = input(f"Pick a number between {MIN_NUMBER}-{MAX_NUMBER}!")
                else:
                    print("Your number was less than the hidden number.")
                    guess = input(f"Pick a number between {MIN_NUMBER}-{MAX_NUMBER}!")
        else:
            print("Please enter a value.")


main()
