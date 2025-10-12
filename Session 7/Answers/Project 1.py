import random

# Start Function
def davar(score_ai, score_human):
    if score_ai > score_human:
        print(f"Score AI = {score_ai} | Score Human = {score_human} | AI is winner !")
    elif score_human > score_ai:
        print(f"Score AI = {score_ai} | Score Human = {score_human} | Human is winner !")
    else:
        print(f"Score AI = {score_ai} | Score Human = {score_human} | Equal")

def ai_choice():
    entekhabha = ["rock", "paper", "scissors"]
    return random.choice(entekhabha)

def qoli_save_data(txt):
    with open("RPC_results.txt", "a") as file:
        file.write(txt + "\n")

# End Function

# Start Main
ai_score = 0
human_score = 0

for i in range(1, 6):
    human_choice = input(f"Round {i} | Enter your choice : ").lower()
    entekhab_ai = ai_choice()
    print("-------------------")
    # Nested conditions
    if human_choice == entekhab_ai:
        print("Equal !")
        qoli_save_data("Equal !")

    elif human_choice == "rock":
        if entekhab_ai == "scissors":
            human_score += 1
            print(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")
            qoli_save_data(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")
        else:
            ai_score += 1
            print(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")
            qoli_save_data(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")


    elif human_choice == "paper":
        if entekhab_ai == "rock":
            human_score += 1
            print(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")
            qoli_save_data(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")
        else:
            ai_score += 1
            print(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")
            qoli_save_data(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")


    elif human_choice == "Scissors":
        if entekhab_ai == "paper":
            human_score += 1
            print(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")
            qoli_save_data(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is Human")
        else:
            ai_score += 1
            print(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")
            qoli_save_data(f"Round {i} | Human = {human_choice} | AI = {entekhab_ai} | Winner is AI")

    print("-------------------")

davar(ai_score, human_score)

# End Main