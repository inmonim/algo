import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    mat = [input().strip().split() for _ in range(5)]
    
    num_set = set()
    
    for y in range(5):
        for x in range(5):
            # 시작점
            q = [(mat[y][x], y, x)]
            # bfs
            while q:
                cur, py, px = q.pop()
                for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    ny, nx = py+dy, px+dx
                    
                    # 범위 체크
                    if 0 <= ny < 5 and 0 <= nx < 5:
                        # 완성될 문자열이면
                        if len(cur) == 5:
                            num_set.add(cur + mat[ny][nx])
                        # 다음 스택으로 넘기기
                        else:
                            q.append((cur + mat[ny][nx], ny, nx))

    print(num_set)