import random;
from Art import logo;

EASY_LEVEL_ATTEMPTS = 10;
HARD_LEVEL_ATTEMPTS = 5;

def check_the_guess(guessed_number, actual_number):
    """
    Checks answer against guess. Returns the number of turns remaining.
    """
    if guessed_number > 100 :
        print("Wrong attempt! The number should be between 1 and 100.")
        quit();
    if guessed_number == actual_number :
        print(f"You got it! The answer was {actual_number}");
        quit();
    elif guessed_number < actual_number :
        print("Too low.");
    else:
        print("Too high.");

def set_attempts():
    number_of_attempts = 0;
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ");
    if difficulty == "hard":
        number_of_attempts = HARD_LEVEL_ATTEMPTS;
    elif difficulty == "easy" :
        number_of_attempts = EASY_LEVEL_ATTEMPTS;
    else:
        print("Wrong input.");
        quit();

    return number_of_attempts;

def game():
    print(logo);
    print("Welcome to the Number Guessing Game!\nI'm thinking of the number between 1 and 100.");
    attempts = set_attempts();
    number = random.randint(1, 100);

    while True :
        print(f"You have {attempts} attempts remaining to guess the number.");
        guess = int(input("Make a guess: "));
        check_the_guess(guessed_number = guess, actual_number = number);
        attempts -= 1;
        if attempts == 0 :
            print("You've run out of guesses, you lose.")
            break;
        else:
            print("Guess again.")
    print(f"Numnber -> {number}");
game();
