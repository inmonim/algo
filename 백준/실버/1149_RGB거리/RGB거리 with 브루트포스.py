import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N = int(input())
    rgb = [list(map(int, input().split())) for _ in range(N)]

    next_list = [(rgb[0][0], 0), (rgb[0][1], 1), (rgb[0][2], 2)]
    step = 1
    while step < N:
        now_list = next_list
        m = min(next_list)[0] + max(rgb[step])
        next_list = []
        for node in now_list:
            for i in range(3):
                if node[1] != i:
                    v = node[0]+rgb[step][i]
                    if v <= m:
                        next_list.append((v, i))
        step += 1
    print(min(next_list)[0])