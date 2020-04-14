import random

n = int(input('Enter dots num: '))
red = 0
blue = n


class Dot:
    def __init__(self):
        self.x = 0
        self.y = 0


for _ in range(n):
    _ = Dot()
    _.x = random.random()
    _.y = random.random()

    if _.x ** 2 + _.y ** 2 <= 1:
        red += 1

print(4 * red / blue)
