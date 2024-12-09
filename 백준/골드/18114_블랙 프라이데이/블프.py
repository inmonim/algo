import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    from itertools import combinations
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    def s(arr):
        for r in range(1, 4):
            for combo in combinations(arr, r):
                if sum(combo) == m:
                    return 1
                
        return 0

    print(s(arr))