import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N = int(input())
    arr = list(map(int, input().split()))
    s_l = sorted(list({i:0 for i in arr}.keys()))
    i_d = {v:i for i, v in enumerate(s_l)}
    ans = [str(i_d[i]) for i in arr]

    print(' '.join(ans))