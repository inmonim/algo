import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys, heapq

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    
    min_q, max_q = [], []
    
    visited = [0] * N
    
    for i in range(N):
        o, n = input().split()
        n = int(n)
        
        if o == 'I':
            heapq.heappush(min_q, (n, i))
            heapq.heappush(max_q, (-n, i))
            visited[i] = 1
        else:
            if n == -1 and min_q:
                visited[heapq.heappop(min_q)[1]] = 0
            elif n == 1 and max_q:
                visited[heapq.heappop(max_q)[1]] = 0
        while max_q and visited[max_q[0][1]] == 0:
            heapq.heappop(max_q)
        while min_q and visited[min_q[0][1]] == 0:
            heapq.heappop(min_q)
    
    if not max_q:
        print('EMPTY')
    else:
        print(f'{-max_q[0][0]} {min_q[0][0]}')