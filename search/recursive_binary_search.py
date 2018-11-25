def recursive_binary_search(list_, target):
    lenght = len(list_)
    return _recursive_binary_search(list_, target, 0, lenght)


def _recursive_binary_search(list_, target, start, end):
    if start == end:
        return None
    else:
        midle = (end + start) // 2
        value = list_[midle]
        if value == target:
            return midle
        elif value > target:
            return _recursive_binary_search(list_, target, start, midle)
        else:
            return _recursive_binary_search(list_, target, midle + 1, end)
