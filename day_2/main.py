from helper.main import read_data, TEST_FILE, FILE

print("Day 2 results:")

OPPONENT_ROCK = 'A'
OPPONENT_PAPER = 'B'
OPPONENT_SCISSORS = 'C'

MY_ROCK = 'X'
MY_PAPER = 'Y'
MY_SCISSORS = 'Z'

ROCK = 'R'
PAPER = 'P'
SCISSORS = 'S'
"""
Combinations
"""
SYMBOLS = {
    ROCK: {'symbols': [OPPONENT_ROCK, MY_ROCK], 'points': 1},
    PAPER: {'symbols': [OPPONENT_PAPER, MY_PAPER], 'points': 2},
    SCISSORS: {'symbols': [OPPONENT_SCISSORS, MY_SCISSORS], 'points': 3}
}

SCENARIOS = [
    {
        'options': [ROCK, SCISSORS],
        'win': ROCK,
        'lose': SCISSORS
    },
    {
        'options': [ROCK, PAPER],
        'win': PAPER,
        'lose': ROCK
    },
    {
        'options': [PAPER, SCISSORS],
        'win': SCISSORS,
        'lose': PAPER
    },
    {
        'options': [PAPER, SCISSORS],
        'win': SCISSORS,
        'lose': PAPER
    }
]

LOSE = 0
DRAW = 3
WIN = 6

test_data = read_data(TEST_FILE)


def calculate_win(data: [str], strategy=None):
    sanitize_data = [x.replace("\n", '').split(" ") for x in data]

    sum = 0
    for game_round in sanitize_data:
        player_1 = recognize_symbol(game_round[0])
        player_2 = recognize_symbol(game_round[1])

        if strategy is not None:
            player_2 = strategy(player_1, game_round[1])

        sum += calculate_round(player_1, player_2)

    return sum


def calculate_round(player1: str, player2: str):
    if player1 == player2:
        return DRAW + SYMBOLS.get(player2).get('points')

    scenario = find_scenario([player1, player2])

    if scenario.get('win') == player1:
        return LOSE + SYMBOLS.get(player2).get('points')

    if scenario.get('win') == player2:
        return WIN + SYMBOLS.get(player2).get('points')


def recognize_symbol(symbol: str):
    for k, v in SYMBOLS.items():
        if symbol in v.get('symbols'):
            return k


def find_scenario(players: list[str]):
    for scenario in SCENARIOS:
        if players[0] in scenario.get('options') and players[1] in scenario.get('options'):
            return scenario


assert PAPER == recognize_symbol(OPPONENT_PAPER)
assert ROCK == recognize_symbol(OPPONENT_ROCK)
assert SCISSORS == recognize_symbol(MY_SCISSORS)
assert SCENARIOS[0] == find_scenario([SCISSORS, ROCK])
assert SCENARIOS[1] == find_scenario([ROCK, PAPER])
assert 8 == calculate_round(ROCK, PAPER)
assert 1 == calculate_round(PAPER, ROCK)
assert 15 == calculate_win(test_data)

assert 10718 == calculate_win(read_data(FILE))

"""
Part TWO
 X means you need to lose, 
 Y means you need to end the round in a draw, and
 Z means you need to win. Good luck!"
"""
STRATEGY = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}


def strategy(player1: str, expected_result):
    """
    Find scenario for action
    """
    if expected_result == 'Y':
        return player1

    if expected_result == 'X':
        for scenario in SCENARIOS:
            if scenario.get('win') == player1:
                return scenario.get('lose')

    if expected_result == 'Z':
        for scenario in SCENARIOS:
            if scenario.get('lose') == player1:
                return scenario.get('win')


assert 12 == calculate_win(test_data, strategy)
print(calculate_win(read_data(FILE), strategy))
