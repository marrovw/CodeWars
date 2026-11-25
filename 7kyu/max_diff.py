# https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095
def max_diff(lst):
    if len(lst) > 1:
        return sorted(lst)[-1] - sorted(lst)[0]
    else:
        return 0