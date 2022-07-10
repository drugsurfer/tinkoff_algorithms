# Сортировка вставками
'''
Зададим указатель i и пройдёмся им по массиву со 2 до n-го элемента,
на каждом шаге будем смещать выбранный элемент влево до тех пор, пока
его можно двигать и элемент слева больше него
'''
n = int(input())
nums = list(map(int, input().split()))
for i in range(1, n):
    k = i
    while k > 0 and nums[k - 1] > nums[k]:
        nums[k], nums[k - 1] = nums[k - 1], nums[k]
        k -= 1
print(' '.join(map(str, nums)))