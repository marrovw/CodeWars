# https://www.codewars.com/kata/57a083a57cb1f31db7000028
def powers_of_two(n):
    result = []
    for element in range(n + 1):
        result.append(2 ** element)
    return result