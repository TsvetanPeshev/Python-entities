from art import logo;
def caesar(cipher_text, shift_amount, choise_of_direction) :
    text_as_list = [];
    divider = 26;

    for letter in cipher_text :
        if shift_amount % divider == 0 :
            divider-= 1;
        temp = shift_amount % divider;
        print(temp)
        if choise_of_direction == "decode" :
            temp *= -1;
        letter_as_integer = ord(letter) + temp;
        character = chr(letter_as_integer);
        text_as_list.append(character);

    print(f"{choise_of_direction}d message: {''.join(text_as_list)}.");

print(logo)
restart = "yes";

while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n");
    text = input("Type your message:\n").lower();
    shift = int(input("Type the shift number:\n"));
    caesar(cipher_text = text, shift_amount = shift, choise_of_direction = direction);
    restart = input("Do you want to restart the program? Type 'yes' for restart or 'no' for quit.\n").lower();
print("Goodbye!");
