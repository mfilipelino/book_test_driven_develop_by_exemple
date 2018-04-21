def max_item(lst):

    def _max_item(lst, size):
        if size == 0:
            return []
        elif size == 1:
            return lst[0]
        else:
            head, *tail = lst
            if head > tail[0]:
                tail[0] = head
            return _max_item(tail, size - 1)

    return _max_item(lst, size=len(lst))
