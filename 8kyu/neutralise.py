def neutralise(s1, s2):
    result = ''
    for i in range(len(s1)):
        if s1[i] == '+' and s2[i] == '+':
            result += '+'
        elif s1[i] == '-' and s2[i] == '-':
            result += '-'
        else:
            result += '0'
    return result