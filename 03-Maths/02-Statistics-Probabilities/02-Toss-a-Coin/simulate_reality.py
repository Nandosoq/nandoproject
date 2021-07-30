# pylint: disable=missing-docstring

import random

def play_one_game(n_toss):
    '''TO DO: return the number of heads'''
    number_of_heads = 0

    for i in range(n_toss):
        number_of_heads += random.randint(0, 1)

    return number_of_heads


def play_n_game(n_games, n_toss):
    '''The keys will be the possible head counts of each game
    The values will correspond to the probability of a game ending with that
     number of heads.
    '''

    dict_play_n_game = {}
    list_play_n_game = []

    for i in range(n_games):
        list_play_n_game.append(play_one_game(n_toss))

    for v in range(n_toss + 1):
        dict_play_n_game[v] = list_play_n_game.count(v) / n_games

    return dict_play_n_game
