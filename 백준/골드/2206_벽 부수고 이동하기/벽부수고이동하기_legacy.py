import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    n, m = map(int, input().split())

    arr = [list(input().strip()) for _ in range(n)]
    dyx = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    arr[0][0] = 1

    def bfs(start, isf):
        Q = start
        while Q:
            y, x = Q.pop(0)
            for dy, dx in dyx:
                ny, nx = y+dy, x+dx
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                
                if arr[ny][nx] == '0' or (type(arr[ny][nx]) == int and arr[ny][nx] >= arr[y][x]+1):
                    arr[ny][nx] = arr[y][x] + 1
                    if ny == n-1 and nx == m-1:
                        if isf:
                            return arr[ny][nx] - break_wall(arr, 0)
                        return arr[ny][nx]
                    Q.append((ny, nx))

        if isf:
            next_list = break_wall(arr, 1)
            score = -1
            for w_yx in next_list:
                wy, wx = w_yx
                arr[wy][wx] = '0'
                score = max(score, bfs([(0, 0)], 0))
                arr[wy][wx] = '1'
            return score
        return -1
        
    def break_wall(arr, f):
        min_v = 0
        next_list = []
        Q = [(0, 0)]
        while Q:
            y, x = Q.pop(0)
            for dy, dx in dyx:
                ny, nx = dy+y, dx+x
                if ny < 0 or nx < 0 or ny >= n or nx >= m:
                    continue
                if type(arr[ny][nx]) == int and arr[ny][nx] > arr[y][x]:
                    Q.append((ny, nx))
                    continue
                if arr[ny][nx] == '1':
                    dny, dnx = dy+ny, dx+nx
                    if dny < 0 or dnx < 0 or dny >= n or dnx >= m:
                        continue
                    if arr[dny][dnx] == '0':
                        next_list.append((ny, nx))
                    elif type(arr[dny][dnx]) == int and arr[dny][dnx] > arr[y][x]:
                        min_v = max(min_v, arr[dny][dnx] - (arr[y][x]+2))
        
        if f:
            return next_list
        return min_v

    v = bfs([(0, 0)], 1)

    print(v)