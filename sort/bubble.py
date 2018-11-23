
def bubble_sort(lst):
    size = len(lst)
    if size < 2:
        return lst
    else:
        return _bubble_sort(size, lst)


def _bubble_sort(size, lst):
    for i in range(1, size):
        for j in range(size - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
