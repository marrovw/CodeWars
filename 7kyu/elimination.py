def elimination(arr):
    for i in arr:
        if arr.count(i) == 2:
        #список.count(элемент_списка) выводит количество этого элемента в списке
            return i
    return None