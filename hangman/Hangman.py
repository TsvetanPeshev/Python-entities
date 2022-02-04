import random
from Hangman_words import word_list;
from Hangman_art import logo, stages;

import time;
start_time = time.time();
choosen_word = random.choice(word_list);
display = [];
lives = 6;
contain_the_letter = False;


for i in range(len(choosen_word)):
    display.append('_');

print(logo);
print("Pssst, the solution is joyful.")

while '_' in display and (lives > 0):
    guess = input("Guess a letter: ").lower();

    if guess in display :
        print(f"You've already guessed '{guess}'.");
        continue;

    for i in range(len(choosen_word)) :
        if choosen_word[i] == guess :
            display[i] = choosen_word[i];
            contain_the_letter = True;

    print(f"{' '.join(display)}")

    if contain_the_letter == False :
        lives -= 1;
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print(stages[lives])
    else:
        contain_the_letter = False;

if lives == 0 :
    print("You lose.\nGame Over!");
else:
    print("You win.\nGame Over!");
print("---%s seconds ---" % (time.time() - start_time));
