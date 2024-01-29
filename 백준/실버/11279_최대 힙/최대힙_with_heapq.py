import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time
import heapq

@stdin_time
def sol(input):

    oper = [int(input()) for _ in range(int(input()))]

    Q = []

    for o in oper:
        if not o:
            if Q:
                print(-heapq.heappop(Q))
            else:
                print(0)
        else:
            heapq.heappush(Q, -o)