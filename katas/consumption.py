from decimal import *


def consumption(km, l):
    getcontext().prec = 3
    return Decimal(km) / Decimal(l)