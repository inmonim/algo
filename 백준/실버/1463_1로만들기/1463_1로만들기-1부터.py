import sys
import os

path = os.path.dirname(os.path.realpath(__file__))
input_file = path+"/input.txt"

sys.stdin = open(input_file)

# n = sys.stdin.readline()

n = int(input())
visited={}
cnt = 0
Q = [1]

while Q:
    if n in Q:
        break
    cnt += 1
    n_num = []
    for i in Q:
        if i*3 not in visited and i*3 < n:
            n_num.append(i*3)
            visited[i*3] = 1
        if i*2 not in visited and i*2 < n:
            n_num.append(i*2)
            visited[i*2] = 1
        if i+1 not in visited:
            n_num.append(i+1)
    Q = n_num
    print(visited)


print(cnt)