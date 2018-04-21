"""
source: https://www.urionlinejudge.com.br/repository/UOJ_1044.html
level: beginner
type: sequencial
"""


def multiples(a, b):
    if a > b:
        a, b = b, a
    return b % a == 0


if __name__ == '__main__':
    a, b = map(int, input().split())
    if multiples(a, b):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')