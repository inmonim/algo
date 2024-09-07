import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time
from pprint import pprint

@stdin_time
def sol(input):

    N, K = int(input()), int(input())

    s, e = 1, K
    a = 0

    while s <= e:
        
        m = (s + e) // 2
        cnt = 0
        for i in range(1, N+1):
            cnt += min(m//i, N)
        
        if cnt > K:
            a = m
            e = m-1
        elif cnt == K:
            a = m
            break
        else:
            s = m+1

    print(a)