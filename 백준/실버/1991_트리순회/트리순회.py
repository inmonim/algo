import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n = int(input())

    tree = dict()
    # 혹시 모른다 순서대로 안 줄지
    tree[1] = 'A'
    tree['A'] = 1
    for _ in range(n):
        c, l, r = input().split()
        ci = tree[c]
        if l != '.':
            tree[ci*2] = l
            tree[l] = ci*2
        if r != '.':
            tree[ci*2+1] = r
            tree[r] = ci*2+1

    def pre(s, i):
        s += tree[i]
        if i * 2 in tree and tree[i*2] != '.':
            s = pre(s, i*2)
        if i * 2 + 1 in tree and tree[i * 2 + 1] != '.':
            s = pre(s, i*2+1)
        return s

    def ino(s, i):
        if i *2 in tree and tree[i*2] != '.':
            s = ino(s, i*2)
        s += tree[i]
        if i * 2 + 1 in tree and tree[i * 2 + 1] != '.':
            s = ino(s, i*2+1)
        return s

    def pos(s, i):
        if i *2 in tree and tree[i*2] != '.':
            s = pos(s, i*2)
        if i * 2 + 1 in tree and tree[i * 2 + 1] != '.':
            s = pos(s, i*2+1)
        s += tree[i]
        return s

    print(pre('', 1))
    print(ino('', 1))
    print(pos('', 1))