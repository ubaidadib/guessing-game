#Guessing Game

import random
attempts_list = []


#function to show score
def show_score():
    if not attempts_list:
        print("There's currently no high score, start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")


attempts = 0
rand_number = random.randint(1, 10) #generates random number between 1 and 10

print("Hello player! Welcome to the guessing game!")
player_name = input("What's your name? ")
wanna_play = input(
    f"Hi, {player_name}, would you like to play the guessing game?"
    " (Enter Yes/No): "
).lower()

if wanna_play == "no" or wanna_play == "No":
    show_score()
    exit()
else:
    while wanna_play == "yes":
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            if(guess < 1 or guess > 10):
                raise ValueError("Please guess a number within the given range")

            attempts += 1
            attempts_list.append(attempts)


            if(guess == rand_number):
                print("Nice, you got it!")
                print(f"It took you {attempts} attempts!")
                wanna_play = input("Would you like to play again (Enter Yes/No): " ).lower()
            else:
                print("That's not it, try again!")
        except ValueError as err:
            print(err) 

    show_score()





