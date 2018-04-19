def remaining_value(value, coin):
    return float('%.2f' % (value % coin))


def number_of_coins(value, coin):
    return value // coin


def notes(money, notes_values):
    pass

def notes_and_coins(money):
    notes =[2.0, 5.0, 10.0, 20.0, 50.0, 100.0]
    while notes != []:
