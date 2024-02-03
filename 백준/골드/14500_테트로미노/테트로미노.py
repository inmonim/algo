import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N, M = map(int, input().split())

    def check(y, x, tetro):
        score = mat[y][x]
        for dy, dx in tetro:
            ny, nx = dy+y, dx+x
        
            try:
                score += mat[ny][nx]
            except:
                return 0
        return score

    square = [(0, 1), (1, 0), (1, 1)]
    x_thunder = [(0, 1), (1, 1), (1, 2)]
    y_thunder = [(1, 0), (1, 1), (2, 1)]
    r_x_thunder = [(0, 1), (-1, 1), (-1, 2)]
    r_y_thunder = [(1, 0), (1, -1), (2, -1)]
    r = [(0, 1), (0, 2), (1, 2)]
    s = [(1, 0), (1, 1), (1, 2)]
    r_r = [(0, 1), (1, 0), (0, 2)]
    s_r = [(0, 1), (1, 0), (2, 0)]
    y_r = [(0, 1), (1, 1), (2, 1)]
    y_s = [(1, 0), (2, 0), (2, 1)]
    ㅣ = [(1,0), (2,0), (3,0)]
    ㅡ = [(0,1), (0,2), (0,3)]
    ㅜ = [(0, 1), (0, 2), (1, 1)]
    ㅏ = [(1, 0), (1, 1), (2, 0)]
    ㅗ = [(0, 1), (-1, 1), (0, 2)]
    ㅓ = [(1, 0), (1, -1), (2, 0)]
    r_ㄱ = [(0, 1), (0, 2), (-1, 2)]
    r_ㄴ = [(1, 0), (2, 0), (2, -1)]

    tetro_list = [square, x_thunder, r_x_thunder, r_y_thunder, y_thunder, r, s, y_r, y_s, ㅣ, ㅡ, r_r, s_r, ㅜ, ㅏ, ㅗ, ㅓ, r_ㄱ,r_ㄴ]

    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
        
    ans = 0
    for y in range(N):
        for x in range(M):
            for tetro in tetro_list:
                score = check(y, x, tetro)
                if score > ans:
                    ans = score

    print(ans)