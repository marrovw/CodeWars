# https://www.codewars.com/kata/56a25ba95df27b7743000016
def validate_code(code):
    if str(code)[0] == '1' or str(code)[0] == '2' or str(code)[0] == '3':
        return True
    else:
        return False