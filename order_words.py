def order_word(s):
    if s == "" or s == None:
        s = 'Invalid String!'
        return s
    else:
        s = sorted(s)
        return "".join(s)
    #sorted -> список символов по ASCII (из строки в список)
    # join -> склеивает в строку (из списка в строку)