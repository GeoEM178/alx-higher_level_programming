#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        tari = 0
    else:
        tari = 32
    print('{}'.format(chr(i - tari)), end='')
