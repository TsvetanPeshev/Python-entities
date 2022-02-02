import random;
print("Welcome to the PyPassword Generator!");
try :
    number_of_letters = int(input("How many letters would you like in your password?\n"));
    number_of_symols = int(input("How many symbols would you like?\n"));
    number_of_numbers = int(input("How many numbers would you like?\n"));
except :
    print("Incorrect input! Input should be a digit!")
    quit();
total_lenght = number_of_letters + number_of_numbers + number_of_symols;
password = list();
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+'];

for letter in range(0, number_of_letters) :
    password.append(random.choice(letters));

for symbol in range(0, number_of_symols) :
    password.append(random.choice(symbols));

for number in range(0, number_of_numbers) :
    password.append(random.choice(numbers));


s = "";
# s1 = "";
random.shuffle(password);
# for element in password :
#     s1 += str(element);

for i in range(0, len(password)):
    e = password.pop(random.randint(0, len(password) - 1));
    s += str(e);
print(f"Here is your password: {s}");
# print(f"Here is your password: {s1}");
