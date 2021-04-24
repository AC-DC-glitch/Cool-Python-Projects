import random

guess_num = random.randint(1, 100)

user_guess = int(input("Try to guess the number!! It lies between 1 and 100. You have 5 guesses, so use them "
                       "carefully! :"))
guess_count = 0

while user_guess != guess_num and guess_count < 4:
    if user_guess < guess_num:
        print("The number you are looking for is greater than",  user_guess, "!")

    elif user_guess > guess_num:
        print("The number you are looking for is lesser than", user_guess, "!")

    guess_count += 1
    user_guess = int(input("Try another time!:"))

if guess_count < 4 and user_guess == guess_num:
    print("Congrats! You have beaten the system")
else:
    print("Sorry! YOU LOSE, the number was", guess_num)
