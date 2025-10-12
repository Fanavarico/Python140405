import tkinter as tk

# ---------- Global Variables ----------
player1_score = 0
player2_score = 0
round_number = 1


# ---------- Functions ----------
def play_round():
    global player1_score, player2_score, round_number

    p1 = entry_p1.get().lower()
    p2 = entry_p2.get().lower()

    # validate input
    if p1 not in ["rock", "paper", "scissors"] or p2 not in ["rock", "paper", "scissors"]:
        lbl_result.config(text="❌ Invalid input! Please enter rock, paper, or scissors.")
        return

    # Determine the winner
    if p1 == p2:
        result = "It's a tie!"
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        player1_score += 1
        result = f"✅ Player 1 wins Round {round_number}!"
    else:
        player2_score += 1
        result = f"✅ Player 2 wins Round {round_number}!"

    # Update labels
    lbl_result.config(text=result, fg="black")
    lbl_score.config(text=f"Player 1: {player1_score} | Player 2: {player2_score}", fg="black")
    lbl_round.config(text=f"Round {round_number}", fg="black")
    round_number += 1

    # Clear inputs
    entry_p1.delete(0, tk.END)
    entry_p2.delete(0, tk.END)


# ---------- GUI ----------
root = tk.Tk()
root.title("Rock Paper Scissors - 2 Player")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#f5f5f5")

# Round Label
lbl_round = tk.Label(root, text="Round 1", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="black")
lbl_round.place(x=160, y=10)

# Player 1 Entry
lbl_p1 = tk.Label(root, text="Player 1 Choice:", bg="#f5f5f5", fg="black")
lbl_p1.place(x=50, y=60)
entry_p1 = tk.Entry(root, width=15)
entry_p1.place(x=180, y=60)

# Player 2 Entry
lbl_p2 = tk.Label(root, text="Player 2 Choice:", bg="#f5f5f5", fg="black")
lbl_p2.place(x=50, y=100)
entry_p2 = tk.Entry(root, width=15)
entry_p2.place(x=180, y=100)

# Play Button
btn_play = tk.Button(root, text="Play Round", command=play_round, width=15)
btn_play.place(x=140, y=140)

# Result Label
lbl_result = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5", fg="black")
lbl_result.place(x=80, y=190)

# Score Label
lbl_score = tk.Label(root, text="Player 1: 0 | Player 2: 0", font=("Arial", 12, "bold"), bg="#f5f5f5", fg="black")
lbl_score.place(x=110, y=230)

# Run App
root.mainloop()