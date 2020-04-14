import random

n = int(input('Enter dots num: '))
red = 0
blue = n

for _ in range(n):
    x = random.random()
    y = random.random()

    if x ** 2 + y ** 2 <= 1:
        red += 1

print(4 * red / blue)
