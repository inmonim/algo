import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

# 오히려 일찍 나온 7569번 토마토 문제보다 간단한 2차원 배열 BFS 문제다.

# 2차원 배열 내의 익은 토마토가 1일 뒤 상하좌우의 토마토도 익게 만든다면

# 모든 토마토를 익히는 데 며칠이 소모되는가?

# 비어있는 칸도 있으며, 그에 따라 모든 토마토를 익힐 수 없는 경우 -1 출력

import sys

input = sys.stdin.readline

X, Y = map(int, input().split())

now, arr, t, cnt = [], [], 0, 0

for y in range(Y):
    arr.append(input().split())
    for x in range(X):
        if arr[y][x] == '0':
            t += 1
        elif arr[y][x] == '1':
            now.append((y, x))

while now:
    tom = []
    for y, x in now:
        for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if arr[ny][nx] == '0':
                    tom.append((ny, nx))
                    arr[ny][nx] = '1'
                    t -= 1
    if tom:
        cnt += 1
    now = tom

cnt = -1 if t else cnt

print(cnt)