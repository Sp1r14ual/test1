import numpy as np
numbers = list(np.random.randint(low=1, high=10, size=100000))

#Сортируем список за O(nlogn)
numbers.sort()
index = 0

#Пока индекс не выйдет за границы массива, проверяем числа
while index is not None:

    #Поскольку список уже отсортирован, нам достаточно проверить, что следующее число совпадает с текущим
    number_in_tail = numbers[index] == numbers[index + 1]
    print(index, numbers[index], number_in_tail)
    
    #Записываем в index индекс первого вхождения следующего числа, если числа в списке закончились, то записываем в него None и останавливаем цикл
    try:
        index = numbers.index(numbers[index] + 1)
    except:
        index = None

#Временная сложность алгоритма ~ O(logn)
