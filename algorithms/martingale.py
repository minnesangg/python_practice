import random

HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]

def flip_coin():
    return random.choice(COIN_VALUES)

def martingale(*, starting_funds: int, minimum_bet: int, maximum_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = minimum_bet

    while current_funds > 0:
        steps_to_loose += 1
        current_funds -= current_bet
        flipped_coin = flip_coin()
        if flipped_coin == HEADS:
            win = current_bet * 2
            current_funds += win
            current_bet = minimum_bet
        else:
            current_bet *= 2
            if current_bet > maximum_bet:
                current_bet = minimum_bet
            if current_bet > current_funds:
                current_bet = current_funds

    return steps_to_loose

def simulate_martingale_for_n_players(*, starting_funds: int, minimum_bet: int,
                                      maximum_bet: int, n_games: int) -> float:
    total_steps_to_loose = 0
    for i in range(n_games):
        steps_to_loose = martingale(starting_funds=starting_funds,
                                    minimum_bet=minimum_bet,
                                    maximum_bet=maximum_bet)
        total_steps_to_loose += steps_to_loose

    return total_steps_to_loose / n_games

print(
    simulate_martingale_for_n_players(
        n_games=10,
        starting_funds=1000,
        minimum_bet=1,
        maximum_bet=100
    )
)