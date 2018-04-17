def insertion_sort(lst):

    def sort(lst, size):
        if size == 0:
            return []
        elif size == 1:
            return lst
        elif size == 2:
            a, b = lst
            return [b, a] if a > b else [a, b]
        else:
            ult = size - 1
            for i in range(0, ult):
                if lst[i] > lst[i+1]:
                    lst[i+1], lst[i] = lst[i], lst[i+1]
            tail = sort(lst[:-1], size=size-1)
            head = [lst[ult]]
            return tail + head

    return sort(lst, size=len(lst))
