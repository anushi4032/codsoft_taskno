import tkinter as tk
import random
from tkinter import messagebox


def winner(userchoice, computerchoice):

    if userchoice.lower() == computerchoice.lower():
        return "It's a tie!"
    elif (userchoice.lower() == "rock" and computerchoice.lower() == "scissors") or \
         (userchoice.lower() == "scissors" and computerchoice.lower() == "paper") or \
         (userchoice.lower() == "paper" and computerchoice.lower() == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game(userchoice):
    global user_score, computer_score
    computerchoice = random.choice(["rock", "paper", "scissors"])
    result = winner(userchoice, computerchoice)
    
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
  
    result_label.config(text=f"Your choice: {userchoice.capitalize()}\n" f"Computer's choice: {computerchoice.capitalize()}\n" f"{result}")
    score_label.config(text=f"Your Score: {user_score} | Computer's Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Your Score: 0 | Computer's Score: 0")
    result_label.config(text="Make your choice to begin!")

window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("500x500")

user_score = 0
computer_score = 0

title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial Black", 20, "bold"))
title_label.pack(pady=10)

instructions_label = tk.Label(window, text="Choose your move:", font=("Arial", 12))
instructions_label.pack()

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(window, text="Make your choice to begin!", font=("Boulder", 12,"bold"))
result_label.pack(pady=10)

score_label = tk.Label(window, text=f"Your Score: {user_score} | Computer's Score: {computer_score}", font=("Arial", 12))
score_label.pack()

playagain_button = tk.Button(window, text="Play Again (Reset Scores)", command=reset_game)
playagain_button.pack(pady=10)

window.mainloop()