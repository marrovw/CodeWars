# https://www.codewars.com/kata/5966e33c4e686b508700002d
def sum_str(a: str, b: str) -> str:
    if a == '':
        a = 0
    else:
        a = int(a)
    if b == "":
        b = 0
    else:
        b = int(b)
    c = a + b
    return str(c) 