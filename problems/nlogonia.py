"""
source: https://www.urionlinejudge.com.br/judge/pt/runs/add/1091
level: beginner
level:
"""

def validate_input(number_testes):
    return number_testes > 0 and number_testes <= 1000


def residence_is_located(east_weast, north_south, x, y):
    if east_weast == x or north_south == y:
        return 'divisa'
    elif x < east_weast:
        if y > north_south:
            return 'NO'
        else:
            return 'SO'
    else:
        if y > north_south:
            return 'NE'
        else:
            return 'SE'


def main():
    while True:
        number_tests = int(input())
        if validate_input(number_tests):
            east_weast, north_south = map(int, input().split())
            for i in range(number_tests):
                x, y = map(int, input().split())
                print(residence_is_located(east_weast, north_south, x, y))
        else:
            break


if __name__ == '__main__':
    main()
