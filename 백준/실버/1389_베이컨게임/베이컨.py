import sys
import os

path = os.path.dirname(os.path.realpath(__file__))
input_file = path+"/input.txt"

sys.stdin = open(input_file)

import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

friends = [[] for _ in range(N+1)]
cnt_list = [0] * (N+1)

for i in range(M):
    s, e = map(int, input().split(' '))
    friends[s].append(e)
    friends[e].append(s)

for i in range(1, N+1):
    check = {i : 0}
    Q = [friends[i]]
    cnt = 0
    while Q:
        cnt += 1
        nodes = Q.pop(0)
        new_nodes = []
        for node in nodes:
            if not check.get(node):
                check[node] = cnt
                new_nodes.extend(friends[node])
        if new_nodes:
            Q.append(new_nodes)
        if len(check) == N:
            cnt_list[i] = sum(check.values())

print(cnt_list.index(min(cnt_list[1:])))