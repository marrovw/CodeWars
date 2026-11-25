# https://www.codewars.com/kata/55d7e5aa7b619a86ed000070
def order_word(s):
    if s == "" or s == None:
        s = 'Invalid String!'
        return s
    else:
        s = sorted(s)
        return "".join(s)
    #sorted -> список символов по ASCII (из строки в список)
    # join -> склеивает в строку (из списка в строку)