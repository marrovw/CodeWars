# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b
def reverse_list(l):
    new_l = []
    for i in range(len(l) - 1, -1, -1):
        new_l.append(l[i])
    return new_l