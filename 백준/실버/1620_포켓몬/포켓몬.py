import os
import sys

sys.stdin =  open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys

input = sys.stdin.readline

N,M = map(int, input().split())

n_d = {}
n_d2 = {}
for i in range(N):
    name = input().strip()
    n_d[name] = i+1
    n_d2[name] = i+1
    n_d2[i+1] = name
n_l = [0]+list(n_d.keys())

for i in range(M):
    a = input().strip()
    if a.isdigit():
        print(n_l[int(a)])
    else:
        print(n_d[a])
        
print(sys.getsizeof(n_d))
print(sys.getsizeof(n_l))
print(sys.getsizeof(n_d2))