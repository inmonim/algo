import sys
import os

path = os.path.dirname(os.path.realpath(__file__))
input_file = path+"/input.txt"

sys.stdin = open(input_file)

import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline

N, M = map(int, input().split(' '))

friends = [[] for _ in range(N+1)]
cnt_list = [0] * (N+1)

def dfs(friend, check: dict, cnt):
    new_friend = []
    cnt += 1
    for j in friend:
        if not check.get(j):
            check[j] = cnt
        if  len(check) == N:
            return sum(check.values())
        new_friend.extend(friends[j])
    else:
        ans = dfs(new_friend, check, cnt)
    return ans

for i in range(M):
    s, e = map(int, input().split(' '))
    friends[s].append(e)
    friends[e].append(s)

for i in range(1, N+1):
    check = {}
    cnt = dfs(friends[i], check, 0)
    cnt_list[i] = cnt

print(cnt_list.index(min(cnt_list[1:])))