import os, sys

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys

input = sys.stdin.readline

N = int(input())
route = [[] for _ in range(N+1)]

for i in range(int(input())):
    s, e = map(int, input().split())
    
    route[s].append(e)
    route[e].append(s)

Q = route[1].copy()
visited = [0] * (N+1)
visited[1] = 1

while Q:
    n = Q.pop(0)
    if not visited[n]:
        visited[n] = 1
        Q.extend(route[n])

print(sum(visited[2:]))