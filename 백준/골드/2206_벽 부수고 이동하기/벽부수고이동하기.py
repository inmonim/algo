import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    from collections import deque

    n, m = map(int, input().split())

    arr = [list(input().strip()) for _ in range(n)]
    res = []
    visited = [[0] * m for _ in range(n)]
    dyx = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited[0][0] = 1
    Q = deque([(0, 0)])

    while Q:
        y, x = Q.popleft()
        if y == n-1 and x == m-1:
            res.append(visited[y][x])
        
        for dy, dx in dyx:
            ny, nx = dy+y, dx+x
            if ny >= n or ny < 0 or nx >= m or nx < 0:
                continue
            
            if arr[ny][nx] != '1' and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                Q.append((ny, nx))
            
            elif arr[ny][nx] == '1':
                for dy2, dx2 in dyx:
                    if dy2+dy+dx2+dx == 0:
                        continue
                    dny, dnx = dy2+ny, dx2+nx
                    if dny >= n or dny < 0 or dnx >= m or dnx < 0:
                        continue
                    
                    if arr[dny][dnx] == '0' and visited[dny][dnx] == 0:
                        arr[dny][dnx] = visited[y][x] + 2

    if arr[n-1][m-1] != '0':
        res.append(arr[n-1][m-1])
    visited = [[0] * m for _ in range(n)]
    visited[n-1][m-1] = 1
    Q = deque([(n-1, m-1)])
    arr[n-1][m-1] = 1

    while Q:
        y, x = Q.popleft()
        
        for dy, dx in dyx:
            ny, nx = dy+y, dx+x
            if ny >= n or ny < 0 or nx >= m or nx < 0:
                continue
            
            if arr[ny][nx] == '0' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                arr[ny][nx] = arr[y][x]+1
                Q.append((ny,nx))
            elif arr[ny][nx] != '1' and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                res.append(arr[ny][nx]+arr[y][x])
                arr[ny][nx] = arr[y][x] + 1
                Q.append((ny, nx))
    if not res:
        res.append(-1)

    print(min(res))