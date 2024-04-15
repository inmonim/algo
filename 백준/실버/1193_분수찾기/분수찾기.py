import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n = int(input())

    arr = [0, 1]
    i = 1
    c = 1
    while i <= n:
        i = i+c
        arr.append(i)
        c += 1

    j = arr[-2]
    y = arr.index(j)
    x = n - j
    if y % 2:
        num = y + -x
        den = 1 + x
    else:
        num = 1 + x
        den = y + -x
    print(f'{num}/{den}')