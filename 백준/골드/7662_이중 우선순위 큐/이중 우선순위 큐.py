import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

# 우선 순위 큐를 통해 풀 수 있는 문제 같다.

# 일반적인 우선 순위 큐와 다른 것이라면, 최댓값과 최솟값을 삭제하는 두 가진 연산이 가능하다는 것이다.

# 최솟값이 root인 힙으로 먼저 구현해보자.

import sys

input = sys.stdin.readline

def h_min_add(n, Q):
    Q.append(n)
    i = len(Q)-1
    
    while i >= 2 and Q[i] < Q[i//2]:
        Q[i], Q[i//2] = Q[i//2], Q[i]
        i = i//2
    return Q

def h_max_add(n, Q):
    Q.append(n)
    i = len(Q)-1
    
    while i >= 2 and Q[i] > Q[i//2]:
        Q[i], Q[i//2] = Q[i//2], Q[i]
        i = i//2
    return Q
    
def h_del_min(Q):
    if len(Q) <= 2:
        Q = [0]
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
            return Q
    return Q

def h_del_max(Q):
    if len(Q) <= 2:
        Q = [0]
        return Q
    Q[1] = Q.pop()
    i = 1
    
    while i*2+1 <= len(Q)-1:
        if Q[i] < Q[i*2] or Q[i] < Q[i*2+1]:
            if Q[i*2] < Q[i*2+1]:
                Q[i], Q[i*2+1] = Q[i*2+1], Q[i]
                i = i * 2 + 1
            else:
                Q[i], Q[i*2] = Q[i*2], Q[i]
                i = i * 2
        else:
            return Q
    return Q

for _ in range(int(input())):
    
    N = int(input())
    
    oper = [input().split() for _ in range(N)]
    
    max_q, min_q = [0], [0]
    
    check = 0
    for i in oper:
        if i[0] == 'I':
            check += 1
        elif i[0] == 'D' and check >= 1:
            check -= 1
    
    if check == 0:
        print('EMPTY')
        continue
    
    check = 0
    for i in range(N):
        o, n = oper[i]
        n = int(n)
        
        if o == 'I':
            max_q = h_max_add(n, max_q)
            min_q = h_min_add(n, min_q)
            check += 1
        elif o == 'D':
            if n == -1:
                min_q = h_del_min(min_q)
            else:
                max_q = h_del_max(max_q)
            
            if check > 0:
                check -= 1
                if check == 0:
                    max_q, min_q = [0], [0]

    print(f'{max_q[1]} {min_q[1]}')