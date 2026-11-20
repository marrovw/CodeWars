def powers_of_two(n):
    result = []
    for element in range(n + 1):
        result.append(2 ** element)
    return result