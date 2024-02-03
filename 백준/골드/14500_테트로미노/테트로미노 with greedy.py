import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N, M = map(int, input().split())
    
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    
    d = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    def check(y, x):
        v = 0
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            try:
                if v < mat[ny][nx] and (ny, nx) not in visited:
                    nn = (ny, nx)
                    v = mat[ny][nx]
                    visited[(ny, nx)] = 1
            except:
                continue
        return nn, v
    
    ans = 0
    for y in range(N):
        for x in range(M):
            score = mat[y][x]
            visited = {}
            for _ in range(3):
                nn, v = check(y, x)
                if not nn:
                    break
                score += v
                y, x = nn
            else:
                if score > ans:
                    ans = score
    
    print(ans)