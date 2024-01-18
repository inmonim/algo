import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt")

# 2차원 배열에 0과 1이 주어져있다.

# 상하좌우로 연결된 1은 하나의 통합된 단지다. 대각선은 연결된 것으로 치지 않는다.

# 이렇게 연결된 통합된 단지는 총 몇 개인지 출력하고,

# 각 단지 별 가구 수를 오름차순으로 출력하라.

import sys

input = sys.stdin.readline

N = int(input())

jido = [list(map(int, input().strip())) for _ in range(N)]

visited = jido.copy()

houses = []

def bfs(Q : list):
    house = 0
    while Q:
        y, x = Q.pop(0)
        house += 1
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ny, nx = y+dy, x+dx
            if ny >= 0 and N > ny and nx >= 0 and N > nx:
                if jido[ny][nx] and visited[ny][nx]:
                    visited[ny][nx] = 0
                    Q.append((ny, nx))
    return house

cnt = 0
for y in range(N):
    for x in range(N):
        if jido[y][x] and visited[y][x]:
            visited[y][x] = 0
            cnt += 1
            
            Q = [(y, x)]
            house = bfs(Q)
            houses.append(house)

print(cnt, *sorted(houses), sep='\n')