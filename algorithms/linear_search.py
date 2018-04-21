
def linear_search(target, list_):
    size = len(list_)
    if size == 0:
        return None
    else:
        for i in range(size):
            if target == list_[i]:
                return i
        else:
            return None