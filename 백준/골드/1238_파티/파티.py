import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    from collections import deque

    def bfs(s, t, pre_score):
        m = M*N*2
        visited = [m] * (N+1)
        Q = deque([(s, pre_score)])
        
        while Q:
            i, n = Q.popleft()
            
            for nx in node[i]:
                ni, nn = nx
                nnn = nn+n

                if visited[ni] >= nnn:
                    visited[ni] = nnn
                    if ni == t:
                        m = nnn
                    else:
                        Q.append((ni, nnn))

        return m

    N, M, T = map(int, input().split())
    node = [[] for _ in range(N+1)]

    for _ in range(M):
        s, e, n = map(int, input().split())
        node[s].append((e, n))

    answer = 0

    for start in range(1, N+1):
        if start == T:
            continue
        
        score = bfs(start, T, 0)
        ans = bfs(T, start, score)
        answer = ans if ans > answer else answer

    print(answer)