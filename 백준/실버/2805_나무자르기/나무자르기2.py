import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__))+'/input.txt')

import sys

input = sys.stdin.readline

N, T = map(int, input().split())

trees = list(map(int, input().split()))

d = {}
for t in trees:
    d[t] = d[t]+1 if d.get(t) else 1
    
k = sorted(d.keys())[::-1]
n = 0
mul = 0
for i in range(len(k)-1):
    if n < T:
        mul += d[k[i]]
        n += mul * (k[i] - k[i+1])
        
        if n >= T:
            print(k[i+1] + (n-T)//mul)
            break
else:
    mul += d[k[-1]]
    n += mul * k[-1]
    print((n-T)//mul)