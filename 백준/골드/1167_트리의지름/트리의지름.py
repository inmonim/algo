import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    def bfs(start, end):
        visited = [0 for _ in range(N+1)]
        Q = [(start, 0)]
        while Q:
            n = Q.pop(0)
            i, x = n
            visited[i] = 1
            nn = route[i]
            for k, v in nn.items():
                if not visited[k]:
                    Q.append((k, x + v))
                if k in end:
                    end[k] = x + v
        
        return end

    N = int(input())
    route = {i:dict() for i in range(1, N+1)}
    leaf = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        n = arr[0]
        for i in range(1, len(arr), 2):
            if arr[i] == -1:
                if i == 3:
                    leaf.append(n)
                break
            route[n][arr[i]] = arr[i+1]

    start, end = leaf[0], {i:0 for i in leaf[1:]}
    end = bfs(start, end)

    m = 0
    next_n = 0
    for k, v in end.items():
        if v > m:
            m = v
            next_n = k

    start, end = next_n, {i:0 for i in leaf}
    end.pop(start)

    end = bfs(start, end)

    print(max(end.values()))
    