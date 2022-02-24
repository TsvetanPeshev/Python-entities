from Art import logo;
import random;
import os;

def calculate_score(hand) :
    """
    Take a list of cards and return the score calculated from the cards
    """
    result = 0;

    for i in range(0 , len(hand)) :
        try :
            result += hand[i];
        except:
            if hand[i] == 'A' :
                result += 11;
            else :
                result += 10;
    if hand.count('A') > 0 and result > 21:
        result -= 10;
    return result;

def deal_card() :
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'];
    card = random.choice(cards);
    return card;

def compare(user_score, computer_score):
    message = "";

    if user_score == computer_score :
        message = "Draw";
    elif computer_score == 0 :
        message = "Lose, opponent has a Blackjack";
    elif user_score == 0 :
        message = "Win with a Blackjack"
    elif (user_score > computer_score and user_score < 22) or (user_score < 22 and computer_score > 21) :
        print(f"Inside the loop: User score {user_score}\nComputer score {computer_score}")
        message = "You Win";
    else:
        message = "Bust";

    return message;

def check_for_blackjack(hand, value):
    if hand.count('A') == 1 and hand.count(10) == 1 and len(hand) == 2 :
        value = 0;
    return value;

def play_game():
    user_cards = [];
    computer_cards = [];

    for _ in range(2):
        user_cards.append(deal_card());
        computer_cards.append(deal_card());

    os.system("cls");
    print(logo);
    print(f"Your cards: {user_cards}");
    print(f"Computer's first card: {computer_cards[0]}");
    another_card = input("Type 'y' to get another card, type 'n' to pass: ");

    if another_card == 'y':
        user_cards.append(deal_card());

    user_hand_result = calculate_score(user_cards);
    computer_hand_result = calculate_score(computer_cards);

    while computer_hand_result < 17 :
        computer_cards.append(deal_card());
        computer_hand_result = calculate_score(computer_cards);

    print(f"Your final hand: {user_cards}, final score: {user_hand_result}");
    print(f"Computer's final hand: {computer_cards}, final score: {computer_hand_result}");

    user_hand_result = check_for_blackjack(value = user_hand_result, hand = user_cards);
    computer_hand_result = check_for_blackjack(value = computer_hand_result, hand = computer_cards);

    message_to_print = compare(user_score = user_hand_result, computer_score = computer_hand_result);

    print(message_to_print);

while True:
    continue_to_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ");

    if continue_to_play == 'n' :
        break;

    play_game();
