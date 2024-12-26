import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    from collections import deque

    n, m = map(int, input().split())

    mat = [list(map(int, input().split())) for _ in range(n)]

    q = deque()
    cnt = 0
    answer = -1
    while answer == -1:
        for y in range(n):
            for x in range(m):
                if mat[y][x]:
                    q.append((y, x))
                    break
            if q:
                break
        else:
            answer = 0
        
        visit = [[0] * m for _ in range(n)]
        visit[y][x] = 1
        while q:
            y, x = q.pop()
            
            for ny, nx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if 0 <= ny < n and 0 <= nx < m:
                    if mat[ny][nx] == 0:
                        mat[y][x] -= 1
                        if mat[y][x] == 0:
                            mat[y][x] = -1
                    elif mat[ny][nx] > 0 and not visit[ny][nx]:
                        visit[ny][nx] = 1
                        q.append((ny, nx))
        
        for y in range(n):
            for x in range(m):
                if mat[y][x] < 0:
                    mat[y][x] = 0
                elif mat[y][x] > 0 and not visit[y][x]:
                    answer = cnt
        
        cnt += 1
    print(answer)