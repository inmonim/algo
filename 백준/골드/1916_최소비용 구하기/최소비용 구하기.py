import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    
    import heapq

    N, M = int(input()), int(input())

    node = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, v = map(int, input().split())
        node[s].append((v, e))

    S, E = map(int, input().split())

    visit = [float('inf')] * (N+1)
    Q = []
    heapq.heappush(Q, (0, S))

    while Q:
        v, i = heapq.heappop(Q)
        if v >= visit[E]:
            continue
        for nv, ni in node[i]:
            rv = nv + v
            if visit[ni] > rv:
                visit[ni] = rv
                heapq.heappush(Q, (rv, ni))

    print(visit[E])