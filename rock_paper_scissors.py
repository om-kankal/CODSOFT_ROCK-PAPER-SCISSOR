import tkinter as tk
import random
from tkinter import messagebox
from tkinter import PhotoImage

# Create a window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("900x550")
window.configure(bg="#add8e6")  # Light blue background
window.resizable(0, 0)

# Initializing scores
user_score = 0
computer_score = 0

# Load images
try:
    rock_image = PhotoImage(file="rock.png").subsample(3, 3)
    paper_image = PhotoImage(file="paper.png").subsample(3, 3)
    scissors_image = PhotoImage(file="scissors.png").subsample(3, 3)
except Exception as e:
    messagebox.showerror("Image Error", "Error loading images: " + str(e))


# Function to generate computer's choice randomly
def computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


# Function to check who won the round
def check_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if user == "rock" and computer == "scissors":
        return "You win!"
    if user == "scissors" and computer == "paper":
        return "You win!"
    if user == "paper" and computer == "rock":
        return "You win!"
    return "Computer wins!"


# Function to update scores
def update_scores(result):
    global user_score
    global computer_score
    if result == "You win!":
        user_score += 1
    if result == "Computer wins!":
        computer_score += 1
    score_label.config(text="User: " + str(user_score) + " | Computer: " + str(computer_score))


# Main function to play the turn
def play_game(user_choice):
    global computer_score
    global user_score

    computer = computer_choice()
    result = check_winner(user_choice, computer)

    # Update the scores
    update_scores(result)

    result_label.config(
        text="Your choice: " + user_choice.capitalize() + "\nComputer's choice: " + computer.capitalize() + "\n" + result)

    # Update images based on the choices
    if user_choice == "rock":
        user_image_label.config(image=rock_image)
    elif user_choice == "paper":
        user_image_label.config(image=paper_image)
    elif user_choice == "scissors":
        user_image_label.config(image=scissors_image)

    if computer == "rock":
        computer_image_label.config(image=rock_image)
    elif computer == "paper":
        computer_image_label.config(image=paper_image)
    elif computer == "scissors":
        computer_image_label.config(image=scissors_image)


# Function to reset the game
def reset_game():
    global user_score
    global computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="User: 0 | Computer: 0")
    result_label.config(text="Make your choice!")

    user_image_label.config(image="")
    computer_image_label.config(image="")


# Create the labels for scores and results
score_label = tk.Label(window, text="User: 0 | Computer: 0", font=("Arial", 14), bg="#add8e6", fg="green")
score_label.grid(row=0, column=0, columnspan=3, pady=20)

result_label = tk.Label(window, text="Make your choice!", font=("Arial", 16), bg="#add8e6", fg="black")
result_label.grid(row=1, column=0, columnspan=3, pady=20)

user_image_label = tk.Label(window, bg="#add8e6")
user_image_label.grid(row=2, column=0, padx=20)

computer_image_label = tk.Label(window, bg="#add8e6")
computer_image_label.grid(row=2, column=2, padx=20)

# Create the buttons for rock, paper, and scissors
rock_button = tk.Button(window, text="Rock", font=("Arial", 15), bg="#ff6347", fg="white",
                        command=lambda: play_game("rock"))
rock_button.grid(row=3, column=0, padx=20, pady=20)

paper_button = tk.Button(window, text="Paper", font=("Arial", 15), bg="#3cb371", fg="white",
                         command=lambda: play_game("paper"))
paper_button.grid(row=3, column=1, padx=20, pady=20)

scissors_button = tk.Button(window, text="Scissors", font=("Arial", 15), bg="#1e90ff", fg="white",
                            command=lambda: play_game("scissors"))
scissors_button.grid(row=3, column=2, padx=20, pady=20)

# Button to play again
play_again_button = tk.Button(window, text="Play Again", font=("Arial", 15), bg="#ff1493", fg="white",
                              command=reset_game)
play_again_button.grid(row=4, column=0, columnspan=3, pady=30)

# Make window responsive
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# Start the tkinter main loop
window.mainloop()
