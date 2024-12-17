import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n, m = map(int, input().split())
    mat = [input().strip() for _ in range(n)]

    dp = [[0] * m for _ in range(n)]
    max_side = 0

    for y in range(n):
        for x in range(m):
            if mat[y][x] == "1":
                if y == 0 or x == 0:
                    dp[y][x] = 1
                else:
                    dp[y][x] = min(dp[y-1][x], dp[y-1][x-1], dp[y][x-1]) + 1
                max_side = max(max_side, dp[y][x])

    print(max_side**2)