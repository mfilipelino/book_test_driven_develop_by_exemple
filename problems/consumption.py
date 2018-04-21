"""
source: https://www.urionlinejudge.com.br/judge/pt/problems/view/1014
level: beginner
type: sequencial
"""

def output(value):
    return '%.3f km/l' % value


def consumption(km, l):
    return km / l


if __name__ == '__main__':
    km = float(input())
    l = float(input())
    value = consumption(km, l)
    print(output(value))
