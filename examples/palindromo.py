def palindromo(s):
    def _palindromo(lst_str, size):
        if size <= 1:
            return True
        elif size == 2:
            a, b = lst_str
            return True if a == b else False
        else:
            first, *body, last = lst_str
            if first == last:
                return _palindromo(body, size - 2)
            else:
                return False

    return _palindromo(list(s), size=len(s))
