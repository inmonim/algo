import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    from collections import deque

    N, E = map(int, input().split())
    route = deque([[] for _ in range(N+1)])
    for _ in range(E):
        s, e, d = map(int, input().split())
        route[s].append((e, d))
        route[e].append((s, d))

    t1, t2 = map(int, input().split())

    def bfs(s, pre_s, t):
        if s == t:
            return pre_s
        ts = 1000*E*2+1
        visited = [1000*E*2 for _ in range(N+1)]
        Q = deque([(s, pre_s)])
        while Q:
            i, n = Q.popleft()
            visited[i] = n
            
            for node in route[i]:
                ni, nn = node
                nnn = nn + n
                if visited[ni] > nnn and ts > nnn:
                    if ni == t:
                        ts = nnn
                    Q.append((ni, nnn))
                    visited[ni] = nnn
        if ts == 1000*E*2+1:
            ts = -1
        return ts

    def switch(a, b):
        a_s = bfs(1, 0, a)
        if a_s == -1:
            return -1
        a_s_b_s = bfs(a, a_s, b)
        if a_s_b_s == -1:
            return -1
        ans = bfs(b, a_s_b_s, N)
        if ans == -1:
            return -1
        return ans

    ans = [switch(t1, t2), switch(t2, t1)]
    if -1 in ans:
        print(max(ans))
    else:
        print(min(ans))