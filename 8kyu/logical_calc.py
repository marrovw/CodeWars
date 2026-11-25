# https://www.codewars.com/kata/57096af70dad013aa200007b
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