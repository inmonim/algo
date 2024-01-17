import sys
import os

path = os.path.dirname(os.path.realpath(__file__))
input_file = path+"/input.txt"

sys.stdin = open(input_file)

# n = sys.stdin.readline()

n = int(input())
visited={}
cnt = 0
Q = [n]

while Q:
    n_num = []
    for i in Q:
        if i == 1:
            Q = 0
            break
        if not i%3 and i%3 not in visited:
            n_num.append(i//3)
            visited[i//3] = 1
        if not i%2 and i%2 not in visited:
            n_num.append(i//2)
            visited[i//2] = 1
        if i-1 not in visited:
            n_num.append(i-1)
    else:
        Q = n_num
        cnt += 1

print(cnt)