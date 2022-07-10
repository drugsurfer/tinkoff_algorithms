'''
Приближенный двоичный поиск
'''


def bin_search(array, target):
    l, r = -1, len(array)
    while r - l > 1:
        mid = (l + r) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            r = mid
        else:
            l = mid
    if l < 0: # если зн-ие -1 не изменится то правая граница просто сдвинется в начало массива
        return r
    if r == len(array) or abs(target - array[l]) < abs(target - array[r]):
        return l
    return r


array = [1, 4, 5, 6, 8, 9, 10, 14]
print(bin_search(array, 7))

