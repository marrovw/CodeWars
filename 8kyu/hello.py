# https://www.codewars.com/kata/57e3f79c9cb119374600046b
def hello(name=""):
    if len(name) >= 1:
        return "Hello, " + name[0].upper() + name[1:].lower() + '!'
    else:
        return 'Hello, World!'