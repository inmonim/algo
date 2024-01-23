import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

# 3차원 배열로 볼 수 있는, 쌓아올려진 2차원 배열 수납장에 토마토가 저장되어 있다.

# 익은 토마토는 앞, 뒤, 양옆, 위, 아래에 영향을 주어, 다음 날 토마토를 익게 만든다.

# 모든 토마토가 익으려면 며칠이 필요한가?

# 공간이 비어있을 수도 있다. 따라서 토마토가 절대 익지 않는 경우가 발생하는데 이럴 경우 -1을 출력한다.

import sys

input = sys.stdin.readline

X, Z, Y = map(int, input().split())

target = 0
day = []
mat = []
cnt = 0
for i in range(Y):
    arr = []
    for j in range(Z):
        arr.append(list(map(int, input().split())))
        for h in range(X):
            t = arr[-1][h]
            if t == 1:
                day.append([i, j, h])
            elif t == 0:
                target += 1
    mat.append(arr)
    
while day:
    tom = []
    
    for y, z, x in day:
        for dy, dz, dx in ([0,1,0], [0,-1,0], [0,0,1], [0,0,-1], [1, 0, 0], [-1, 0, 0]):
            ny, nz, nx = y+dy, z+dz, x+dx
            
            if 0 <= ny < Y and 0 <= nx < X and 0 <= nz < Z:
                if mat[ny][nz][nx] == 0:
                    mat[ny][nz][nx] = 1
                    tom.append([ny, nz, nx])
                    target -= 1
    if len(tom) >= 1:
        cnt += 1
    day = tom

cnt = -1 if target > 0 else cnt
print(cnt)