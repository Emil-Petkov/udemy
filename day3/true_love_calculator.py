print("Welcome to the Love Calculator!\n")

name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

concatenation_names = name1 + name2

count_letters_true = {
    "t": 0,
    "r": 0,
    "u": 0,
    "e": 0,
}

count_letters_love = {
    "l": 0,
    "o": 0,
    "v": 0,
    "e": 0,
}

for letter in concatenation_names:
    if letter in count_letters_true:
        count_letters_true[letter] += 1

for letter in concatenation_names:
    if letter in count_letters_love:
        count_letters_love[letter] += 1

sum_of_true = sum([l for l in count_letters_true.values()])
sum_of_love = sum([l for l in count_letters_love.values()])

score = str(sum_of_true) + str(sum_of_love)

if int(score) >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif int(score) >= 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")
