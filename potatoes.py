def potatoes(p0, w0, p1):
    x = w0 * (100 - p0) / 100
    y = 100 - p1
    z = x * 100 / y
    return int(z)