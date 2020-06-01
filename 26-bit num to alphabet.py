def trans26(x):
    symbol = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while True:
        r = x % 26
        x = x // 26
        symbol += alphabet[r]
        if x == 0:
            break

    print(symbol[::-1])

trans26(27)

'''
A = 0
B = 1
Z = 25
and so on.
'''
