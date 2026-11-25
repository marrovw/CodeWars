# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
def expression_matter(a, b, c):
    top = []
    top.append(a * b * c)
    top.append(a + b + c)
    top.append(a * (b + c))
    top.append((a + b) * c)
    return max(top)