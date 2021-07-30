# pylint: disable=missing-docstring

import math

def count_possibilities(n_toss, n_heads):
    '''TO DO: return the number of possibilities to get n_heads when flipping the coin n_toss times
        Ex: count_possibilities(4, 4)  = 1'''
    return math.factorial(n_toss) / (math.factorial(n_heads) *
                                     math.factorial(n_toss - n_heads))


def count_total_possibilities(n_toss):
    '''TO DO: return the total amount of different combinations when flipping the coins n_toss times
        Ex: count_total_possibilities(3) = 8'''
    return 2**n_toss


def probability(n_toss):
    '''TO DO: return a dictionary. The keys will be the possible number of heads in each game,
            so they can't be over `n_toss` or under 0. The values for each of those keys will correspond
            to the probability of a game ending with that result.
      probability(5) = {0: ..., 1:..., 2:..., 3:..., 4:..., 5:...}'''

    dict_prob = {}
    t_poss = count_total_possibilities(n_toss)

    for h in range(n_toss + 1):
        dict_prob[h] = count_possibilities(n_toss, h) / t_poss

    return dict_prob
