# https://www.codewars.com/kata/563b74ddd19a3ad462000054
def stringy(size):
    result = ''
    for element in range(1, size + 1):
        if element % 2 == 0:
            result += '0'
        else:
            result += '1'
    return result