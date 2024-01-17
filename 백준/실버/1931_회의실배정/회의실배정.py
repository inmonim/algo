import os, sys

txt = os.path.dirname(os.path.realpath(__file__))+'/input.txt'

sys.stdin = open(txt)

import sys

input = sys.stdin.readline

l = {}

for i in range(int(input())):
    s,e = map(int, input().split())
    l[s] = l[s]+[e] if l.get(s) else [e]

a = 1
c = 0
k = sorted(l.keys())

t = l[k[0]].pop(0)
while c < len(k):
    i = k[c]
    if i >= t:
        a += 1
        if l[i] and l[i][0] == i:
            t = l[i].pop(0)
            continue
        elif l[i]:
            t = l[i].pop(0)
        
    elif t > min(l[i]):
        t = l[i].pop(0)
    c += 1
    print(l)

print(a)