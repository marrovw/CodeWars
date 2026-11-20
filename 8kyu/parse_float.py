def parse_float(string):
    try: # try проверяет код который может вызвать ошибку
        return float(string)
    except (ValueError, TypeError): # действия при ошибке
        return None