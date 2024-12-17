import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n, m = map(int, input().split())

    mat = [input() for _ in range(n)]

    max_w = 1

    for y in range(n):
        if n - (y + 1) < max_w:
            break
        for x in range(m):
            cur_w = 1
            if mat[y][x] == '1' and m-(x+1) > max_w:
                for i in range(1, m-x):
                    if mat[y][x+i] == '0':
                        break
                    cur_w += 1
                    if cur_w > max_w:
                        for yy in range(1, cur_w):
                            f = 0
                            for xx in range(cur_w):
                                if mat[y+yy][x+xx] == "0":
                                    f = 1
                                    break
                            if f:
                                break
                        else:
                            max_w = cur_w

    print(max_w*max_w)