import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
  
    N = int(input())

    routes = [list(map(int, input().split())) for _ in range(N)]
    nodes = [[] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if routes[y][x]:
                nodes[y].append(x)

    for i in range(N):
        routes = nodes[i].copy()
        visited = [0] * N
        answer = [0] * N
        while routes:
            next_node = routes.pop()
            answer[next_node] = 1
            if nodes[next_node] and not visited[next_node]:
                routes.extend(nodes[next_node])
            visited[next_node] = 1
        print(' '.join(map(str, answer)))