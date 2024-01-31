import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N, M = map(int, input().split())

    node = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        
        node[s].append(e)
        node[e].append(s)

    cnt = sum([0 if x else 1 for x in node])-1
        
    for i in range(len(node)):
        if len(node[i]) >= 1:
            stack = node[i]
            while stack:
                route = stack.pop()
                if node[route]:
                    stack.extend(node[route])
                    node[route] = []
            cnt += 1
    print(cnt)