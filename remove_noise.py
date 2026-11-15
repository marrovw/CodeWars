def remove_noise(st):
    noise = '%$&/#·@|º\ª'
    result = []
    for symbol in st:
        if symbol in noise: # in проверяет есть ли symbol в списке/строке noise
            continue
        else:
            result.append(symbol)
    return ''.join(result)