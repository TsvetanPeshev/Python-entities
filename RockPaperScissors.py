import random;
errorMessage = "The input should be a digit between 0 and 2 !";
try :
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"));
except:
    print(errorMessage);
    quit();
random_choice_of_the_program = random.randint(0, 2);
if user_choice < 0 or user_choice > 2 :
    print(errorMessage);
    quit();
rock ="""
     _______
 ---'    ___)
        (____)
        (____)
        (___)
 ---.___(__)\n""";

scissors = """
     _______
 ---'   ____)____
           ______)
          ________)
         (____)
 ---.____(___)\n
          """;
paper = """
     _______
 ---'   ____)____
           ______)
        __________)
        _________)
 ---.__________)\n
 """;

graphics = [rock, paper, scissors];

print(graphics[user_choice]);
print(f"Computer choose:\n{graphics[random_choice_of_the_program]}");


if (user_choice == 2 and random_choice_of_the_program == 0) or (user_choice < random_choice_of_the_program) :
    print("You lose!");
elif user_choice is random_choice_of_the_program :
    print("It's a draw!");
else :
    print("You win!");
