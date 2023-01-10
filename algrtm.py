class Search():
    '''линейный поиск - самый простой поиск.
    Для работы алгоритма поиска не требуется подготовка элементов'''
    def linear(arr, element):
        for i in range (len(arr)):
            if arr[i] == element:
                return i
    
        return -1


    '''двоичный (бинарный) поиск - требуется сортировка в порядке возрастания
        Алгоритм сравнивает значение центрального элемента массива с искомым.
        Если значение совпадают, поиск завершается.
        Иначе 2 варианта:
            1) Если искомое больше, то поиск продолжается справа от центрального элемента массива.
            2) Если искомое меньше, то поиск продолжается слева.
    '''
    def bin_search(arr, element):
        left = 0
        right = len(arr)-1
        index = -1
        while (left <= right) and (index == -1):
            mid = (left + right)//2
            
            if arr[mid] == element:
                index = mid
            else:
                if element<arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return index
    '''
    Поиск прыжками - все элементы должны быть в порядке возрастания.
    Алгоритм сравнивает искомое значение с элементами,
    расположенными друг от друга на определенном расстоянии.

    Расстояние считывается по формуле sqrt(N).
    Для массива из 16 элементов шаг = 4.
    Сравнения происходят до тех пор,
    пока элемент не покажется меньше элемента массива.

    После этого необходимо вернуться на шаг назад и применить линейный поиск.
    
    '''
    def jump (arr, element):
        length = len(arr)
        jump = int (math.sqrt(length))
        left, right = 0, 0
        while left < length and arr[left] <=element:
            right = min(length -1, left+jump)
            if arr[left]<=element and arr[right] >= element:
                break
            left += jump
        if left>= length or arr[left]>element:
            return -1
        right = min(length -1, right)
        i = left
        while i <= right and arr[i] <=element:
            if arr[i] == element:
                return i
            i += 1
        return -1

    
    '''
    Интерполяционный поиск - все элементы должны быть в порядке возрастания.
    Алгоритм предсказывает местонахождение элемента в массиве.
    Работа алгоритма похожа на бумажный словарь.
    Если мы ищем слово на букву "Б", то мы откроем словарь в начале.

    Алгоритм сравнивает искомое с элементом под определенным индексом.
    Индекс расчитывается по формуле A + ((F - arr[A]) * (B-A)) / (arr[B]-arr[A]),
        где F - искомое число, А - нулевой индекс, В - последний индекс массива.
    
    '''

    def interpolation(arr, element):
        left = 0
        right = len(arr) - 1
        while left <= right and element >= arr[left] and element <= arr[right]:
            index = left + int(((float(right - left)/(arr[right] - arr[left])) * (element - arr[left])))
            if arr[index] == element:
                return index
            if arr[index] <element:
                left = index + 1
            else:
                right = index -1
        return -1

    def exponent_search(arr, element):
        if arr[0] == element:
            return 0
        index = 1
        while index <len(arr) and arr[index] <=element:
            index = index * 2
        return binary_search(arr[:min(index,len(arr))], element)

class Sorting():

    def bubble_sort(arr):
        n = len(arr)

        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    b = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = b
        return arr
    def selectrion_sort(arr):
        for i in range (len(arr)):
            min_index = i
            for j in range (i+1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    def insertion_search(arr):
        for i in range(1, len(arr)):
            element_to_insert = arr[i]
            j = i - 1
            while j > 0 and arr[j] > element_to_insert:
                arr[j+1] = arr[j]
                j -=1
            arr[j+1] = element_to_insert
        return arr
    #где то тут должна быть сортировка слиянием

    def gnome(arr):
        i, size = 1, len(arr)
        while i < size:
            if arr[i -1] <= arr[i]:
                i += 1
            else:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                if i > 1:
                    i -= 1
        return arr

    
        
#вычислить факториал числа
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)