import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

    rank = 1

    for i in range(1, len(arr)):
        if arr[i-1][0] == m:
            print(rank)
            break
        elif arr[i-1][1:] != arr[i][1:]:
            rank = i + 1
    else:
        print(rank)