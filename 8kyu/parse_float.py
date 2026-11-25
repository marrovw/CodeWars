# https://www.codewars.com/kata/57a386117cb1f31890000039
def parse_float(string):
    try: # try проверяет код который может вызвать ошибку
        return float(string)
    except (ValueError, TypeError): # действия при ошибке
        return None