import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    
    S = [0]*21
    S1 = [i for i in range(21)]
    for _ in range(int(input())):
        op = input().split()
        if len(op) == 1:
            if op[0][0] == 'a':
                S = S1.copy()
            else:
                S = [0]*21
            continue
        o, n = op
        n = int(n)
        if o[0] == 'a':
            S[n] = 1
        elif o[0] == 'r':
            S[n] = 0
        elif o[0] == 'c':
            if S[n]:
                print(1)
            else:
                print(0)
        elif o[0] == 't':
            S[n] = 0 if S[n] else 1