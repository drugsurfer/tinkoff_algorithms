# Реализация линейной структуры: стек
x = []
s = input()
while s != 'exit':
    cmd = s.split()
    if cmd[0] == 'push':
        x.append(cmd[-1])
        print('ok')
    elif cmd[0] == 'pop':
        if len(x) != 0:
            print(x[-1])
            x.pop()
        else:
            print('error')
    elif cmd[0] == 'back':
        if len(x) != 0:
            print(x[-1])
        else:
            print('error')
    elif cmd[0] == 'clear':
        x.clear()
        print('ok')
    s = input()
print('bye')