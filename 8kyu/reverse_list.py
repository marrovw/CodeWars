def reverse_list(l):
    new_l = []
    for i in range(len(l) - 1, -1, -1):
        new_l.append(l[i])
    return new_l