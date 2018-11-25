def log2(n):
    if n == 1:
        return 0
    else:
        x = 2
        i = 1
        while x <= n:
            i += 1
            x += x
        return i
