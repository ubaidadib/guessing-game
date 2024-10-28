import random

# List to store the number of attempts for each game
attempts_list = []

def show_score():
    #Function to display the current high score.
    if not attempts_list:
        print("There's currently no high score, start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts.")

 #Generates a random number between 1 and 10.
def get_random_number():
    return random.randint(1, 10)

#Main function to handle the guessing game logic.
def play_game():
    attempts = 0
    rand_number = get_random_number()

    print(" *********************************** \n Guessing Game started! Try to guess the number\n ***********************************")

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: ").strip())
            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number within the given range (1-10).")
            
            attempts += 1

            if guess == rand_number:
                print(f"Nice! You've guessed the right number {rand_number} in {attempts} attempts!")
                attempts_list.append(attempts)
                break
            else:
                if guess < rand_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
        except ValueError as e:
            print(e)

def main():
    #Main function to control the game flow.
    print("Hello player! Welcome to the guessing game!")
    player_name = input("What's your name? ").strip()
    print(f"Hi, {player_name}! Let's begin the game.")

    while True:
        wanna_play = input("Would you like to play the guessing game? (Enter Yes/No): ").strip().lower()

        if wanna_play == "yes":
            show_score()
            play_game()
        elif wanna_play == "no":
            print("Thanks for playing! See you next time.")
            show_score()
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

if __name__ == "__main__":
    main()
