"""
source: https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
level: beginner
type: sequencial
"""


def remaining_value(value, coin):
    return float('%.2f' % (value % coin))


def number_of_coins(value, coin):
    return value // coin


def change_coin(money, coin):
    number_coins = 0
    if money >= coin:
        number_coins = number_of_coins(money, coin)
    remaining = remaining_value(money, coin)
    return number_coins, remaining


def change_coins(money, coins):
    result = []
    coins = list(reversed(coins))
    while len(coins) > 0:
        coin = coins.pop()
        number_coin, money = change_coin(money, coin)
        result.append(int(number_coin))
    return result


def out_notas(data):
    notas = """NOTAS:
{} nota(s) de R$ 100.00
{} nota(s) de R$ 50.00
{} nota(s) de R$ 20.00
{} nota(s) de R$ 10.00
{} nota(s) de R$ 5.00
{} nota(s) de R$ 2.00
"""
    return notas.format(*data)

