# Реализация простой очереди
b, f = [], []
s = input()
while s != 'exit':
    cmd = s.split()
    if cmd[0] == 'push':
        b.append(cmd[-1])
        print('ok')
    elif cmd[0] == 'pop':
        if len(f) == 0:
            f = list(reversed(b))
            b = []
        print(f[-1])
        f.pop()
    elif cmd[0] == 'front':
        if len(f) == 0:
            f = list(reversed(b))
            b = []
        print(f[-1])
    elif cmd[0] == 'size':
        print(len(f) + len(b))
    elif cmd[0] == 'clear':
        f = []
        b = []
        print('ok')
    s = input()
print('bye')
