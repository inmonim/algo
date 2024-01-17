import sys
import os

path = os.path.dirname(os.path.realpath(__file__))
input_file = path+"/input.txt"

sys.stdin = open(input_file)

# ====================================================

import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split(' '))

cnt = 1

maps = [str(input().strip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

next_moves = [(0, 0)]
f = 0

while next_moves:
    cnt += 1
    moves = next_moves
    next_moves = []
    
    for y, x in moves:
        
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
                      
            if ny >= N or ny < 0 or nx >= M or nx < 0:
                continue
            
            if maps[ny][nx] == '1' and visited[ny][nx] == 0:

                if ny == N-1 and nx == M-1:
                    next_moves.clear()
                    f = 1
                    break
                
                next_moves.append([ny, nx])
                visited[ny][nx] = 1
        if f:
            break
    
print(cnt)