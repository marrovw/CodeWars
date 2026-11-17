def expression_matter(a, b, c):
    top = []
    top.append(a * b * c)
    top.append(a + b + c)
    top.append(a * (b + c))
    top.append((a + b) * c)
    return max(top)