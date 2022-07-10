'''
1041A codeforce
'''

n = int(input())
numbers = list(map(int, input().split()))
x = min(numbers)
print(max(numbers) - (x + n - 1))