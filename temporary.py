import sys
from string import ascii_lowercase
for i in bytes(str(sys.stdin), encoding='utf-8').decode('utf-8'):
    print(i)
std = bytearray(str(sys.stdin), encoding='UTF-8')
print('          00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f')
print('')
size = len(std) // 16 + 1
st = ''
if len(std) % 16 != 0:
    st += '#' * (len(std) // 16 + len(std) % 16)
globalcount = 0
for i in range(size):
    if i < 10:
        print('0000' + str(i) + '0    ', end='')
    else:
        print('0000' + ascii_lowercase[i - 10] + '0    ', end='')
    count = 0
    for j in std[globalcount:]:
        if count < 16:
            print(j, end=' ')
            count += 1
        else:
            break
    if len(st) != 0 and i == size - 1:
        print((16 - len(st)) * '   ', end='')
    print('    ', end='')
    if i == size - 1:
        print(len(st) * ' ', end='')
    if i == size - 1:
        for j in std[globalcount:]:
            if j.isprintable():
                print(j, end='')
            else:
                print('.', end='')
    else:
        for j in std[globalcount: globalcount + 16]:
            if j.isprintable():
                print(j, end='')
            else:
                print('.', end='')
    if i != size - 1:
        print('')
    globalcount += count
