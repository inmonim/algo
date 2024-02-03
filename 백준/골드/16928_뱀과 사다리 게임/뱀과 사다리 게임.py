import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time


@stdin_time
def sol(input):
    N, M = map(int, input().split())

    def bfs():
        for x in now_list:
            for i in range(1, 7):
                if x+i >= 100:
                    print(cnt)
                    next_list.clear()
                    return 
                if arr[x+i]:
                    next_list.append(arr[x+i])
                    if i == 6:
                        while i > 1:
                            i -= 1
                            if not arr[x+i]:
                                next_list.append(x+i)
                                break
                                
                elif i == 6:
                    next_list.append(x+i)

    cnt = 1
    arr = [0] * 101
    for _ in range(N):
        x, y = map(int, input().split())
        arr[x] = y
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x] = y

    now_list = []
    next_list = [1]
    while next_list:
        now_list = next_list
        next_list = []
        bfs()
        cnt += 1