def logical_calc(array, op):
    x = array[0]
    for i in array[1:]:
        if op == "AND":
            x = x and i
        elif op == 'OR':
            x = x or i
        elif op == 'XOR':
            x = x != i
    return x