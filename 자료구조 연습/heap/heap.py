import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys

input = sys.stdin.readline

def h_min_add(n):
    Q.append(n)
    i = len(Q)-1
    
    while i >= 2 and Q[i] < Q[i//2]:
        Q[i], Q[i//2] = Q[i//2], Q[i]
        i = i//2

def h_max_add(n):
    Q.append(n)
    i = len(Q)-1
    
    while i >= 2 and Q[i] > Q[i//2]:
        Q[i], Q[i//2] = Q[i//2], Q[i]
        i = i//2
    
def h_del_min():
    if len(Q) <= 2:
        Q.pop()
        return Q
    Q[1] = Q.pop()
    i = 1
    
    while i*2+1 <= len(Q)-1:
        if Q[i] > Q[i*2] or Q[i] > Q[i*2+1]:
            if Q[i*2] > Q[i*2+1]:
                Q[i], Q[i*2+1] = Q[i*2+1], Q[i]
                i = i * 2 + 1
            else:
                Q[i], Q[i*2] = Q[i*2], Q[i]
                i = i * 2
        else:
            break

def h_del_max():
    if len(Q) == 2:
        Q.pop()
        return Q
    Q[1] = Q.pop()
    i = 1
    
    while i*2+1 <= len(Q)-1:
        if Q[i] < Q[i*2] or Q[i] < Q[i*2+1]:
            if Q[i*2] > Q[i*2+1]:
                Q[i], Q[i*2+1] = Q[i*2+1], Q[i]
                i = i * 2 + 1
            else:
                Q[i], Q[i*2] = Q[i*2], Q[i]
                i = i * 2
        else:
            break
                
Q = [0]

for _ in range(int(input())):
    
    n = int(input())
    h_max_add(n)
    print(Q)


for _ in range(15):
    h_del_max()
    print(Q)