import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n = int(input())
    num = list(map(int, input().split()))
    a = float('inf')
    for i in range(n):
        y = max(num) * num[i]
        if not sum(y % num[j] for j in range(n)):
            a = min(a, y)
    print(a)