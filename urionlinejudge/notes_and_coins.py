def remaining_value(value, coin):
    return float('%.2f' % (value % coin))


def number_of_coins(value, coin):
    return value // coin


def notes_and_coins(money):
    pass