import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time


@stdin_time
def sol(input):

    n = int(input())

    m = int(n ** 0.5)
    cnt = 4
    def rec(n, m, depth):
        global cnt
        for i in range(m, 0, -1):
            n2 = n
            if i ** 2 <= n:
                n2 -= i**2
                if n2:
                    if depth == 4:
                        return
                    rec(n2, i, depth+1)
                else:
                    cnt = min(cnt, depth)
                    if cnt == 1:
                        return
    rec(n, m, 1)
    print(cnt)