'''
Письма
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
prefix_sum = [0] * (len(a) + 1)
for i in range(1, len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]
for num in b:
    l, r = -1, n
    while r - l > 1:
        mid = (l + r) // 2
        if prefix_sum[mid] < num:
            l = mid
        else:
            r = mid
    if l < 0:
        print(f'{1} {num}')
    else:
        print(f'{l + 1} {num - prefix_sum[l]}')


