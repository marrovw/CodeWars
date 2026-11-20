def string_clean(s):
    new_s = ""
    for i in s:
        if i.isdigit():
            pass
        else:
            new_s = new_s + i
    return new_s