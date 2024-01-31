import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    acc_sum = [0] * (N+1)
    acc_sum[1] = arr[0]

    for i in range(2, N+1):
        acc_sum[i] = acc_sum[i-1]+arr[i-1]
        
    for _ in range(M):
        s, e = map(int, input().split())
        print(acc_sum[e] - acc_sum[s-1])