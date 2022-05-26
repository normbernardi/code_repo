import random
rps_dict = {('rock', 'paper'): -1, ('rock', 'scissors'): 1, ('rock', 'rock'): 0,
            ('paper', 'scissors'): -1, ('paper', 'rock'): 1, ('paper', 'paper'): 0,
            ('scissors', 'rock'): -1, ('scissors', 'paper'): 1, ('scissors', 'scissors'): 0}


def rps() -> int:
    player_one, player_two = rps_choice(), rps_choice()
    print(player_one + ', ' + player_two)
    return rps_dict[(player_one, player_two)]


def rps_choice() -> str:
    return random.choice(["rock", "paper", "scissors"])


print(rps())
print('----------------')
print(rps())
print('----------------')
print(rps())
print('----------------')
print(rps())
print('----------------')
print(rps())
