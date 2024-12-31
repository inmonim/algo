import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time
from pprint import pprint
@stdin_time
def func(input):
    
    # 별 거 없이 쉬운 bfs 문제.
    # 정답 코드 작성에 20분.
    # S랑 D 반대로 받아들여서 "이거 왜 안 돼" 하는 데 40분.
    def sol():
        n, m = map(int, input().split())
        mat = [[0] * m for _ in range(n)]
        
        water = []
        q = []
        
        for i in range(n):
            s = input().strip()
            for ii in range(m):
                mat[i][ii] = s[ii]
                if s[ii] == '*':
                    mat[i][ii] = -1
                    water.append((i, ii))
                elif s[ii] == 'S':
                    q.append((i, ii))
        cnt = 0
        while q:
            cnt += 1
            pre_w = []
            for y, x in water:
                for ny, nx in [(y+1,x), (y-1, x), (y, x+1), (y, x-1)]:
                    if 0 <= ny < n and 0 <= nx < m:
                        if mat[ny][nx] in ['.', 0]:
                            mat[ny][nx] = -1
                            pre_w.append((ny, nx))
            water = pre_w
            pre_q = []
            for y, x in q:
                for ny, nx in [(y+1,x), (y-1, x), (y, x+1), (y, x-1)]:
                    if 0 <= ny < n and 0 <= nx < m:
                        if mat[ny][nx] == 'D':
                            return cnt
                        elif mat[ny][nx] == '.':
                            mat[ny][nx] = 0
                            pre_q.append((ny, nx))
            q = pre_q
        return "KAKTUS"

    print(sol())