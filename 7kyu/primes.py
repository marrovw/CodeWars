# https://www.codewars.com/kata/5681bc8d17af37f50e000015
def primes(start: int, end: int) -> list[int] | None:
    numbers = list(range(start, end + 1))
    result = []

    for number in numbers:
        if number < 2:
            continue

        is_prime = True
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            result.append(number)

    if len(result) > 0:
        return result
    else:
        return None