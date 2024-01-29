import sys, os, time

sys.stdin = open(os.path.dirname(os.path.realpath(__file__))+'/input.txt')

import sys

input = sys.stdin.readline

s_t = time.time()

def h_pop(Q):
    p = Q[1]
    Q[1] = Q[-1]
    Q.pop()
    i = 1
    while i*2 < len(Q):
        lc, rc = i*2, i*2+1
        if lc == len(Q)-1:
            if Q[i] < Q[lc]:
                Q[i], Q[lc] = Q[lc], Q[i]
            return Q, p
        
        if Q[i] <= Q[lc] or Q[i] <= Q[rc]:
            c = lc if Q[lc] > Q[rc] else i*2 + 1
            Q[i], Q[c] = Q[c], Q[i]
            i = c
        else:
            return Q, p
    return Q, p

def h_push(Q, n):
    Q.append(n)
    i = len(Q) - 1
    
    while i > 1:
        if Q[i] >= Q[i//2]:
            Q[i], Q[i//2] = Q[i//2], Q[i]
            i = i//2
        else:
            break
    return Q


oper = [int(input()) for _ in range(int(input()))]

Q = [0]

for o in oper:
    if not o:
        if len(Q) == 1:
            # print(0)
            pass
        else:
            Q, n = h_pop(Q)
            # print(n)
    else:
        Q = h_push(Q, o)
        
e_t = time.time()
ms = e_t - s_t
print(f'\n실행시간: {int(ms*1000)}ms\n')