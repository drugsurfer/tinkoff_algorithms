# Сортировка выбором
'''
Ключевые моменты реализации:
1. Введём указатель k, который будет указывать на начало отсортиро-
ванного участка, изначально k = n − 1
2. Запустим поиск индекса imax максимального значения на отрезке от
0 до k, в конце обменяем ak и aimax
3. Будем повторять до тех пор, пока k > 0
'''

n = int(input())
nums = list(map(int, input().split()))
k = n - 1
while k >= 1:
    i_max = 0
    for i in range(1, k + 1):
        if nums[i] > nums[i_max]:
            i_max = i
    nums[k], nums[i_max] = nums[i_max], nums[k]
    k -= 1
print(' '.join(map(str, nums)))