import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    n = int(input())

    numlist = list(map(int, input().split()))
    dp_min = numlist
    dp_max = numlist
    for _ in range(1, n):
        numlist = list(map(int, input().split()))
        dp_min = [min(dp_min[0], dp_min[1]) + numlist[0],
                    min(dp_min) + numlist[1],
                    min(dp_min[1], dp_min[2]) + numlist[2]]
        dp_max = [max(dp_max[0], dp_max[1]) + numlist[0],
                    max(dp_max) + numlist[1],
                    max(dp_max[1], dp_max[2]) + numlist[2]]
    print(max(dp_max), min(dp_min))
