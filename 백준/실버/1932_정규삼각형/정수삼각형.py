import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n = int(input())
    res = [int(input())]+[0]*n

    for i in range(1, n):
        print(res)
        tmp = res[:]
        num = list(map(int, input().split()))
        
        res[0] = tmp[0] + num[0]
        res[i] = tmp[i-1] + num[i]
        
        for j in range(1, i):
            res[j] = max(tmp[j-1], tmp[j]) + num[j]

    print(max(res))