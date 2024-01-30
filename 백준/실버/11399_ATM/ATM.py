import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N, arr = int(input()), sorted(list(map(int, input().split())))
    a = 0
    for i in range(N):
        a += sum(arr[0:i+1])
    print(a)
    
sol()