from random import randint

def get_integer():
    number = int(input("Enter an integer: "))
    return number

number_to_guess = randint(0, 10)

number_of_guesses = 5

while number_of_guesses > 0:
    try:
        guess = get_integer()
    except ValueError:
        print("You entered a wrong value.")
    else:
        if guess > number_to_guess:
            print("Try again, You entered a greater number")
            number_of_guesses -= 1
        elif guess < number_to_guess:
            print("Try again, You entered a lesser number")
            number_of_guesses -= 1
        elif number_to_guess == guess:
            print("You are cool!")

if number_of_guesses == 0:
    print("You lost, the correct answer: ", number_to_guess)
