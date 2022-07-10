'''
Сортировка подсчетом
'''

n = int(input())
nums = list(map(int, input().split()))
min_,  max_ = min(nums), max(nums)
cnt = [0] * (max_ - min_ + 1)
for num in nums:
    cnt[num - min_] += 1
j = 0
for i in range(len(cnt)):
    for c in range(cnt[i]):
        nums[j] = i + min_
        j += 1
print(' '.join(map(str, nums)))