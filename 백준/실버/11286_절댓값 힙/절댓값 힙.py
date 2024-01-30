import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    import heapq
    
    N = int(input())
    q = []
    for _ in range(N):
        n = int(input())
        
        if not n:
            if q:
                qn = heapq.heappop(q)
                if qn%1:
                    qn = -(int(qn+0.5))
            else:
                qn = 0
            print(qn)
        else:
            if n < 0:
                n = -(n + 0.5)
            heapq.heappush(q, n)