# https://www.codewars.com/kata/57e1e61ba396b3727c000251
def string_clean(s):
    new_s = ""
    for i in s:
        if i.isdigit():
            pass
        else:
            new_s = new_s + i
    return new_s