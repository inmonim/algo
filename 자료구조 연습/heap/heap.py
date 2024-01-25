import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys

input = sys.stdin.readline


def max_heap_add(Q:list, n:int):
    Q.append(n)
    i = len(Q)-1
    while i >= 2 and Q[i] > Q[i//2]:
        Q[i], Q[i//2] = Q[i//2], Q[i]
        i = i//2
    return Q

def min_heap_add(Q: list, n: int):
    Q.append(n)
    i = len(Q) - 1
    while i >= 2 and Q[i] < Q[i//2]:
        Q[i], Q[i//2] = Q[i//2], Q[i]
        i = i//2
    return Q

def max_heap_delete(Q:list):
    if len(Q) <= 2:
        Q = [0]
        return Q
    Q[1] = Q.pop()
    i = 1
    
    while i*2 + 1 < len(Q):
        if i*2 == len(Q)-1:
            if Q[i] < Q[i*2]:
                Q[i], Q[i*2] = Q[i*2], Q[i]
            return Q
        
        if Q[i] <= Q[i*2] and Q[i] <= Q[i*2 + 1]:
            i2 = i*2 if Q[i*2] > Q[i*2+1] else i*2 + 1
            Q[i], Q[i2] = Q[i2], Q[i]
            i = i2
        elif Q[i] <= Q[i*2]:
            Q[i], Q[i*2] = Q[i*2], Q[i]
            i = i*2
        elif Q[i] <= Q[i*2 +1]:
            Q[i], Q[i*2+1] = Q[i*2+1], Q[i]
            i = i*2+1
        else:
            return Q
    return Q

def min_heap_delete(Q:list):
    if len(Q) <= 2:
        Q = [0]
        return Q
    Q[1] = Q.pop()
    i = 1
    
    while i*2 + 1 < len(Q):
        if i*2 == len(Q)-1:
            if Q[i] > Q[i*2]:
                Q[i], Q[i*2] = Q[i*2], Q[i]
            return Q
        
        if Q[i] >= Q[i*2] and Q[i] >= Q[i*2 + 1]:
            i2 = i*2 if Q[i*2] < Q[i*2+1] else i*2 + 1
            Q[i], Q[i2] = Q[i2], Q[i]
            i = i2
        elif Q[i] >= Q[i*2]:
            Q[i], Q[i*2] = Q[i*2], Q[i]
            i = i*2
        elif Q[i] >= Q[i*2 +1]:
            Q[i], Q[i*2+1] = Q[i*2+1], Q[i]
            i = i*2+1
        else:
            return Q
    return Q

max_Q = [0]
min_Q = [0]
for _ in range(int(input())):
    
    n = int(input())
    max_Q = max_heap_add(max_Q, n)
    min_Q = min_heap_add(min_Q, n)

print(min_Q)
for _ in range(5):
    max_Q = max_heap_delete(max_Q)
    min_Q = min_heap_delete(min_Q)
    # print(max_Q)
    print(min_Q)
