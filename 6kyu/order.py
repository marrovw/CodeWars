# https://www.codewars.com/kata/55c45be3b2079eccff00010f
def order(sentence):

    if len(sentence) < 1:
       return ""
    
    sentence = sentence.split() # строка.split(разделитель)
    new_sentence = list(range(len(sentence)))

    for word in sentence:
        for element in word:
            if element.isdigit():
                new_sentence[int(element) - 1] = word #заменяет элемент по индексу в списке

    return ' '.join(new_sentence) # разделитель.join(список)