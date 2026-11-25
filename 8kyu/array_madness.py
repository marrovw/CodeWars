# https://www.codewars.com/kata/56ff6a70e1a63ccdfa0001b1
def array_madness(a,b):

    sum_of_the_squares = 0

    for element in a:
        sum_of_the_squares = sum_of_the_squares + element ** 2

    sum_of_the_cubes = 0

    for element in b:
        sum_of_the_cubes = sum_of_the_cubes + element ** 3
        
    if sum_of_the_squares > sum_of_the_cubes:
        return True
    else:
        return False