import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

import sys, os

sys.stdin = open('./input.txt')

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

f = 0
oy, ox = 0, 0
for y in range(N):
    for x in range(M):
        if mat[y][x] == 2:
            oy, ox = y, x
            f = 1
            break
    if f:
        break

visited = [[0] * M for _ in range(N)]
next_list = [(oy, ox)]
dis = 1
while next_list:
    now_list = next_list.copy()
    next_list = []
    for y, x in now_list:
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and mat[ny][nx]:
                visited[ny][nx] = dis
                next_list.append((ny, nx))
    dis += 1
    
for y in range(N):
    for x in range(M):
        if mat[y][x] and not visited[y][x]:
            visited[y][x] = -1

visited[oy][ox] = 0
for i in range(N):
    print(' '.join(map(str, visited[i])))