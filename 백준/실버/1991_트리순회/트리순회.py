import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n = int(input())

    tree = dict()
    for _ in range(n):
        a,b,c, = input().split()
        tree[a] = (b, c)
    
    def pre(x, i):
        s, t = tree[i]
        x += i
        if s != '.':
            x = pre(x, s)
        if t != '.':
            x = pre(x, t)
        return x
    
    def ino(x, i):
        s, t = tree[i]
        if s != '.':
            x = ino(x, s)
        x += i
        if t != '.':
            x = ino(x, t)
        return x
    
    def pos(x, i):
        s, t = tree[i]
        if s != '.':
            x = pos(x, s)
        if t != '.':
            x = pos(x, t)
        x += i
        return x
        
    print(pre('', 'A'))
    print(ino('', 'A'))
    print(pos('', 'A'))