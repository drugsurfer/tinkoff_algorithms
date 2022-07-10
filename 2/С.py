'''
456A - Ноутбуки
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
z = list(zip(a, b))
z.sort()
flag = 'Poor Alex'
for i in range(len(z)):
    if z[i][1] < z[i - 1][1]:
        flag = 'Happy Alex'
        break
print(flag)