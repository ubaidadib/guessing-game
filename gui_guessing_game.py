import random
import tkinter as tk
from tkinter import messagebox

# List to store the number of attempts for each game
attempts_list = []

class GuessingGameApp:
    def __init__(self, root):
        self.root = root # Reference to the main window
        self.root.title("Guessing Game") # Set the title of the window
        self.root.geometry("400x400") # Set the size of the window
        
        self.attempts = 0 # Initialize the number of attempts to 0
        self.rand_number = self.get_random_number() # Generate a random number

        # Title Label
        self.title_label = tk.Label(root, text="Welcome to the Guessing Game!")
        self.title_label.pack(pady=10)

        # Instruction Label
        self.instruction_label = tk.Label(root, text="Pick a number between 1 and 10:")
        self.instruction_label.pack()

        # Input Field
        self.guess_entry = tk.Entry(root, width=30)
        self.guess_entry.pack(pady=10) # Add padding to the bottom of the entry field

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)

        # Restart Button
        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=5)

        # Message Area to show result feedback
        self.message_label = tk.Label(root, text="", fg="blue")
        self.message_label.pack(pady=5)

        # High Score Display
        self.score_label = tk.Label(root, text="", fg="green")
        self.score_label.pack(pady=5)

        # Display the current high score at the start
        self.show_score()

    def get_random_number(self):
        #Generates a random number between 1 and 10.
        return random.randint(1, 10)

    def show_score(self):
        #Function to display the current high score.
        if not attempts_list:
            self.score_label.config(text="No high score yet, start playing!")
        else:
            self.score_label.config(text=f"High Score: {min(attempts_list)} attempts")

    def check_guess(self):
        #Check the user's guess and provide feedback.
        try:
            guess = int(self.guess_entry.get().strip())

            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number within the given range (1-10).")

            self.attempts += 1

            if guess == self.rand_number:
                self.message_label.config(text=f"Correct! You guessed it in {self.attempts} attempts!", fg="green")
                attempts_list.append(self.attempts)
                self.show_score()
                self.submit_button.config(state="disabled")  # Disable the submit button after a win
            elif guess < self.rand_number:
                self.message_label.config(text="Too low! Try again.", fg="blue")
            else:
                self.message_label.config(text="Too high! Try again.", fg="blue")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 10.")

    def restart_game(self):
        #Reset the game for another round.
        self.rand_number = self.get_random_number()
        self.attempts = 0
        self.guess_entry.delete(0, tk.END)  # Clear the input field
        self.message_label.config(text="")  # Clear the message label
        self.submit_button.config(state="normal")  # Re-enable the submit button


# Create the main window (root) and run the application
root = tk.Tk()
app = GuessingGameApp(root) # Pass the root window to the GuessingGameApp
root.mainloop() # Start the main event loop
