
def recursive_palindromo(ss):
    size = len(ss)
    if len(ss) < 2:
        return True
    elif ss[0] == ss[size - 1]:
        return recursive_palindromo(ss[1:-1])
    else:
        return False