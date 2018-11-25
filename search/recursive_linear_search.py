def recursive_linear_search(list_, target):
    size = len(list_)
    return _recursive_linear_search(list_, target, size)


def _recursive_linear_search(list_, target, size):
    if size == 0:
        return None
    else:
        last = size - 1
        if list_[last] == target:
            return last
        else:
            return _recursive_linear_search(list_, target, last)
