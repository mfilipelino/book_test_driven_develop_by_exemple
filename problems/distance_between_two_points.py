"""
source: https://www.urionlinejudge.com.br/judge/pt/problems/view/1017
level: beginner
type: sequencial
"""


def f1(x1, x2):
    return (x1 - x2) * (x1 - x2)


def square_root(value):
    return value ** 0.5


def distance(x1, y1, x2, y2):
    return square_root(f1(x1, x2) + f1(y1, y2))


def output(value):
    return '%.4f' % value


if __name__ == '__main__':
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    print(output(distance(x1, y1, x2, y2)))
