import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__))+'/input.txt')

import sys

input = sys.stdin.readline

N, T = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort()

Mh =  trees[-1]
mh = 0
h = trees[-1]//2

d = {}

for _ in range(int(trees[-1]**(1/2))):
    i, hi, ri = len(trees)//2, len(trees), 0
    for x in range(int(len(trees)**(1/2))):
        if trees[i] - h == 0:
            break
        elif trees[i] - h > 0:
            i, hi = (i+ri)//2, i
        elif trees[i] - h < 0:
            i, ri = (i+hi)//2, i
    
    t = sum([max(0, trees[i2]-h) for i2 in range(i, len(trees))])
    
    if h not in d:
        d[h] = t
    else:
        print(h)
        break
    
    if t == T:
        print(h)
        break
    elif t > T:
        h, mh = (h+Mh)//2, h
    else:
        h, Mh = (h+mh)//2, h