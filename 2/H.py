'''
Коровы в стойла
'''


def ok(coord, d, k):
    pos, cnt = coord[0], 1
    for i in range(1, len(coord)):
        if pos + d <= coord[i]:
            pos = coord[i]
            cnt += 1
        if cnt == k:
            return True
    return False


def solve(coord, n, k):
    l, r = 0, max(coord)
    while r - l > 1:
        mid = (l + r) // 2
        if ok(coord, mid, k):
            l = mid
        else:
            r = mid
    if ok(coord, r, k):
        return r
    return l


a = [1, 2, 3, 100, 1000]
print(solve(a, 5, 3))


