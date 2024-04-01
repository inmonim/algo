import sys, os, time

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    
    r, c = map(int, input().split())

    alp_set = set()
    map_ = []
    for _ in range(r):
        alpabet = input().strip()
        for i in alpabet:
            alp_set.add(i)
        map_.append(alpabet)

    visited = map_[0][0]
    max_c = len(alp_set)

    def dfs(visited, y, x, res):
        ans = res
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny, nx = dy+y, dx+x
            if 0 > ny or 0 > nx or ny >= r or nx >= c:
                continue
            
            alp = map_[ny][nx]
            if alp not in visited:
                visited += alp
                ans = max(ans, dfs(visited, ny, nx, res+1))
                if ans == max_c:
                    return max_c
                visited = visited[:-1]
        
        return ans

    print(dfs(visited, 0, 0, 1))