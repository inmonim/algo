import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

# 우선 순위 큐를 통해 풀 수 있는 문제 같다.

# 일반적인 우선 순위 큐와 다른 것이라면, 최댓값과 최솟값을 삭제하는 두 가진 연산이 가능하다는 것이다.

# 최솟값이 root인 힙으로 먼저 구현해보자.

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
    
    while i*2 < len(Q):
        lc, rc = i*2, i*2+1
        if lc == len(Q)-1:
            if Q[i] < Q[lc]:
                Q[i], Q[lc] = Q[lc], Q[i]
            return Q
        
        if Q[i] <= Q[lc] or Q[i] <= Q[rc]:
            c = lc if Q[lc] > Q[rc] else i*2 + 1
            Q[i], Q[c] = Q[c], Q[i]
            i = c
        else:
            return Q
    return Q

def min_heap_delete(Q:list):
    if len(Q) <= 2:
        Q = [0]
        return Q
    Q[1] = Q.pop()
    i = 1
    
    while i*2 < len(Q):
        lc, rc = i*2, i*2+1
        if i*2 == len(Q)-1:
            if Q[i] > Q[lc]:
                Q[i], Q[lc] = Q[lc], Q[i]
            return Q
        
        if Q[i] >= Q[lc] or Q[i] >= Q[rc]:
            c = lc if Q[lc] < Q[rc] else rc
            Q[i], Q[c] = Q[c], Q[i]
            i = c
        else:
            return Q
    return Q


for _ in range(int(input())):
    
    N = int(input())
    
    oper = [input().split() for _ in range(N)]
    
    max_q, min_q = [0], [0]

    check = 0
    for i in range(len(oper)):
        o, n = oper[i]
        n = int(n)
        
        if o == 'I':
            check += 1
            max_q = max_heap_add(max_q, n)
            min_q = min_heap_add(min_q, n)
        elif o == 'D':
            if check == 0:
                max_q, min_q = [], []
            elif n == -1:
                min_q = min_heap_delete(min_q)
                check -= 1
            else:
                max_q = max_heap_delete(max_q)
                check -= 1

    if check == 0 or len(max_q) < 1 or len(min_q) < 1:
        print('EMPTY')
    
    else:
        print(f'{max_q[1]} {min_q[1]}')