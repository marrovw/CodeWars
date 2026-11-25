# https://www.codewars.com/kata/56b1f01c247c01db92000076
def double_char(s):
    result = ''
    for symbol in s:
        result = result + symbol + symbol
    return result