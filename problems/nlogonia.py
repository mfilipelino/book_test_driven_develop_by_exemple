import sys


def validate_input(number_testes):
    return number_testes > 0 and number_testes <= 1000


def residence_is_located(east_weast, north_south, x, y):
    if east_weast == x or north_south == y:
        return 'divisa'
    elif x < east_weast:
        if y > north_south:
            return 'N0'
        else:
            return 'S0'
    else:
        if y > north_south:
            return 'NE'
        else:
            return 'SE'


def main(stdin=sys.stdin):

    while True:
        number_tests = int(stdin.readline())
        if validate_input(number_tests):
            east_weast, north_south = map(int, stdin.readline().split())
            for i in range(number_tests):
                x, y = map(int, stdin.readline().split())
                print(residence_is_located(east_weast, north_south, x, y))
        else:
            break


if __name__ == '__main__':
    main()
