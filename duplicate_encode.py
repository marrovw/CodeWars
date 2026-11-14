def duplicate_encode(word):
    word = word.lower()
    x = ''
    for i in word:
        if word.count(i) > 1:
            x += ')'
        else:
            x += '('
    return x