
import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr.sort(key=lambda x:x[1])
    arr.sort(key=lambda x:x[0])

    for i in arr:
        print(*i)