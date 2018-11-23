

def selection(lst):
    size = len(lst)
    if size < 2:
        return lst
    else:
        return _selection(0, size, lst)


def _selection(start, end, lst):

    for i in range(start, end):
        indice_value_min = i
        for j in range(i, end):
            if lst[j] < lst[indice_value_min] :
                indice_value_min = j
        lst[indice_value_min], lst[i] = lst[i], lst[indice_value_min]

    return lst