# https://www.codewars.com/kata/54466996990c921f90000d61
def is_monotone(heights):
    if len(heights) == 0 or len(heights) == 1:
        return True
    maximum = heights[0]
    for i in heights[1::]:
        if i > maximum or i == maximum:
            maximum = i
        else:
            return False
    return True