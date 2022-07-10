# Правильная скобочная последовательность
pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
s = input()
stack = []
for el in s:
    if el not in pairs.keys():
        stack.append(el)
    else:
        if len(stack) == 0:
            break
        else:
            if stack[-1] == pairs[el]:
                stack.pop()
            else:
                break
if len(stack) == 0:
    print('yes')
else:
    print('no')