from Art import logo;
import os;

def find_highest_bidder(bidding_record) :
    max_value = max(bidding_record.values());
    my_reversed_bids = dict(map(reversed, bidding_record.items()));
    print(f"The winner is {my_reversed_bids[max_value]} with a bid of ${max_value}.");

print(logo);
bids = {};
print("Welcome to the secret auction program.");
more_bidders = "yes";

while more_bidders == "yes" :
    name = input("What is your name?: ");
    bid = int(input("What is your bid?: $"));
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.");
    bids[name] = bid;
    os.system("cls");

find_highest_bidder(bidding_record = bids);
