# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {'USDEUR': 0.85,
'GBPEUR': 1.13,
'CHFEUR': 0.86,
'EURGBP': 0.885,
'MXNUSD': 0.05,
'USDMXN': 20,
'CHFUSD': 1.08}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """

    if RATES.get(str(amount[1] + currency) ,0):
        return round(RATES.get(str(amount[1] + currency) ,0) * amount[0])
    #elif RATES.get(str(currency + amount[1]) ,0):
    #    return round(1 / (RATES.get(str(currency + amount[1]), 0) * amount[0]))
    #else:
    return None

    #return round(fx*amount[0])
