rps_win = (('rock', 'scissors'), ('scissors', 'paper', 'paper, rock'))
def rps_evaluate(player_one: str, player_two: str) -> int:
    if player_one == player_two:
        return 0
    elif (player_one, player_two) in rps_win:
        return 1
    else:
        return -1

def player_choice() -> str:
    import random
    return random.choice(["rock", "paper", "scissors"])

def rock_paper_scissors() -> int:
    return rps_evaluate(player_choice(), player_choice())

print(rock_paper_scissors())

