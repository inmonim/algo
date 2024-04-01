import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    
    from collections import deque

    n = int(input())
    node = [[] for _ in range(n+1)]
    for _ in range(n-1):
        s, e, w = map(int, input().split())
        node[s].append((e, w))
        node[e].append((s, w))

    leaf = {}
    s = 1
    for i in range(len(node)):
        if len(node[i]) == 1:
            leaf[i] = 0
            s = i

    def bfs(s):
        Q = deque([(s, 0)])
        visited = [0] * (n+1)
        while Q:
            i, w = Q.popleft()
            visited[i] = 1
            
            for ni, nw in node[i]:
                if not visited[ni]:
                    rw = nw + w
                    if ni in leaf:
                        leaf[ni] = rw
                    Q.append((ni, rw))

        ri, mx = 0, 0
        for k, v in leaf.items():
            if v > mx:
                mx = v
                ri = k

        return (ri, mx)
            
    ri, _ = bfs(s)

    leaf = {i:0 for i in leaf.keys()}

    _, res = bfs(ri)

    print(res)