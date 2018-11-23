
def mergesort(lst):
    size = len(lst)
    if size < 2:
        return lst
    else:
        return _mergesort(lst, size)


def _mergesort(lst, size):

