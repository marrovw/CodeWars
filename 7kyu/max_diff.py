def max_diff(lst):
    if len(lst) > 1:
        return sorted(lst)[-1] - sorted(lst)[0]
    else:
        return 0