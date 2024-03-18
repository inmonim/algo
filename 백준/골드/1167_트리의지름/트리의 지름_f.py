import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

# 트리의 노드 중 가장 먼 노드의 거리를 찾는 문제다.

# 가장 먼 노드는 무조건 리프노드로 한정된다.

# 이진 트리가 아니므로, 리프노드를 찾기 위해서는 연결된 루트가 1개 뿐인 정점을 찾으면 된다.

# 연결된 루트가 1개인 정점 리스트를 만든 뒤, 해당 정점에서 다른 리프노드로 이동할 때 필요한 값을 bfs로 진입하면 될듯하다.

@stdin_time
def sol(input):
    route = {}
    N = int(input())
    start = {}

    for _ in range(N):
        a = list(map(int, input().split()))[:-1]
        route[a[0]] = dict()
        for x in range(1, len(a), 2):
            route[a[0]][a[x]] = a[x+1]
        if len(a) == 3:
            start[a[0]] = 0

    ans = 0
    for s in start.keys():
        visited = [0] * (N +1)
        Q = [(s, 0)]

        while Q:
            node = Q.pop(0)
            visited[node[0]] = 1
            next_node = route[node[0]]
            for k, v in next_node.items():
                if not visited[k]:
                    if k in start:
                        start[k] = node[1] + v
                        continue
                    new_dist = node[1] + v
                    new_node = k
                    Q.append((new_node, new_dist))

        ans = max(ans, max(start.values()))

    print(ans)