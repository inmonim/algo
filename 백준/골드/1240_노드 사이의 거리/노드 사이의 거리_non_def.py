import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    from collections import deque
    n, m = map(int, input().split())
    tree = [{} for _ in range(n+1)]

    for _ in range(n-1):
        s, e, r = map(int, input().split())
        tree[s][e] = r
        tree[e][s] = r

    for _ in range(m):
        s, e = map(int, input().split())
        q = deque([(s, 0)])
        visited = set([s])
        while q:
            ci, cs = q.popleft()
            for k, v in tree[ci].items():
                if k == e:
                    print(cs + v)
                    q = []
                    break
                if k not in visited:
                    visited.add(k)
                    q.append((k, cs + v))
        