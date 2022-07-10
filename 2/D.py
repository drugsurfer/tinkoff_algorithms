'''
Бинарный поиск
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


nums = [1, 2, 4, 6, 7, 10]
print(bin_search(nums, 9))
