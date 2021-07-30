# pylint: disable=missing-docstring

from flip_coin_factorial import probability
from simulate_reality import play_n_game


def mean_squared_error(n_games, n_toss):
    '''TO DO: return the squared error between the theoretical and "actual"
     results (obtained through simulation)'''

    data_n_game = play_n_game(n_games, n_toss)
    data_prob = probability(n_toss)
    data = 0

    for i in range(n_toss):
        data += (data_n_game[i] - data_prob[i])**2

    return data / n_toss
