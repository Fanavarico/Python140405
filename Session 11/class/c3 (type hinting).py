import random

# Syntax
# def name (argument1 : data_type, argument2: data_type) -> data type:


# Start Function
# Type hinting
def davar(score_ai: int, score_human: int) -> None:
    if score_ai > score_human:
        print(f"Score AI = {score_ai} | Score Human = {score_human} | AI is winner !")
    elif score_human > score_ai:
        print(f"Score AI = {score_ai} | Score Human = {score_human} | Human is winner !")
    else:
        print(f"Score AI = {score_ai} | Score Human = {score_human} | Equal")






def ai_choice() -> str:
    entekhabha = ["rock", "paper", "scissors"]
    return random.choice(entekhabha)






def qoli_save_data(txt: str) -> None:
    with open("RPC_results.txt", "a") as file:
        file.write(txt + "\n")






# ["", "", ""]
def update_file_data(index_: int, new_data: list[str]) -> None:
    with open("students_data.txt", "r+") as file:
        total_data = file.readlines()
        # ba try except khatahayi ke rokh mide ro modiriat mikonim
        try:
            total_data[index_] = f"{new_data} \n"
            file.seek(0) # tekon dadan pointer file be avale file
            file.truncate(0) # pak kardan ba etelawt qadimi az index 0 ta akhar file
            file.writelines(total_data) # neveshtan data jadid dakhele file

        except IndexError:
            print("Data not found !")


# union -> (list[str], tuple[int, None])