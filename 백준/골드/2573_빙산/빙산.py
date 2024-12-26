import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time
from pprint import pprint
@stdin_time
def sol(input):
    from collections import deque
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    answer = -1
    cnt = 0
    
    while answer == -1:
        visit = [[0]*m for _ in range(n)]
        q = deque()
        for y in range(n):
            if q:
                break
            for x in range(m):
                if mat[y][x] > 0:
                    q.append((y, x))
                    visit[y][x] = 1
                    break
        # 빙산이 아예 없는(한 번에 없어진) 경우, 0 반환
        else:
            answer = 0
            break
        
        while q:
            y, x = q.pop()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y+dy, x+dx
                if 0 <= ny < n and 0 <= nx < m:
                    # 방문하지 않았고, 빙산이 존재하는 경우
                    if visit[ny][nx] == 0 and mat[ny][nx] > 0:
                        visit[ny][nx] = 1
                        q.append((ny, nx))
                    # 이전 회차에 녹아내린 빙산(-1)은 0으로 수정
                    # 영향을 주는 건 좌우상하이므로, 대각선은 굳이 수정할 필요 없음
                    # 단, 대각선 수정이 없으면 아래의 순회에서 mat[y][x] == 0이 아닌, mat[y][x] <= 0를 조건으로 줘야함
                    elif mat[ny][nx] == -1:
                        mat[ny][nx] = 0
        
        for y in range(n):
            for x in range(m):
                # 바다(0) 또는 수정하지 않은 대각선의 바다(-1) 경우
                if mat[y][x] <= 0:
                    continue
                # 빙산인데 방문한 적이 없다? 너 범인
                if visit[y][x] != 1:
                    answer = cnt
                    break
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < n and 0 <= nx < m:
                        # 상하좌우가 바다인 경우
                        if not mat[ny][nx]:
                            mat[y][x] -= 1
                            # 만약 0이 됐으면, 이번 회차에서 영향을 줄 수 없도록 -1로 수정
                            if not mat[y][x]:
                                mat[y][x] = -1
                                break
        cnt += 1
    print(answer)