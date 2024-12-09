import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)
from module import stdin_time

@stdin_time
def sol(input):
    n = int(input())
    res = [int(input())]
    for i in range(1, n):
        n_res = [0] * (i+1)
        n_list = list(map(int, input().split()))
        
        for ii in range(1, i+1):
            
            n_res[ii-1] = max(res[ii-1] + n_list[ii-1], n_res[ii-1])
            n_res[ii] = res[ii-1] + n_list[ii]
        
        res = n_res[:]

    print(max(res))