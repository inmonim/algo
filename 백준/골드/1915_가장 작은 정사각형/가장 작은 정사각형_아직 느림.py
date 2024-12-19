import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    n, m = map(int, input().split())

    mat = [list(map(int, list(input().strip()))) for _ in range(n)]
    w_list = []

    for y in range(n):
        max_w = 0
        for x in range(m):
            if mat[y][x]:
                max_w += 1
                if max_w >= 2 and max_w <= n - y:
                    w_list.append((y, x-max_w+1, max_w))
            else:
                max_w = 0

    w_list.sort(key=lambda x : x[2])

    answer = 1
    while w_list:
        cur_y, cur_x, cur_w = w_list.pop()
        for y in range(1, cur_w):
            if sum(mat[y+cur_y][cur_x:cur_x+cur_w]) != cur_w:
                break
        else:
            answer = cur_w
            break

    print(answer**2)