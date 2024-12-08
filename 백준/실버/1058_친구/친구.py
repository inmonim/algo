import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N = int(input())

    tmp = [input().strip() for _ in range(N)]

    arr = [0] * N
    for i in range(N):
        cur_arr = []
        for j in range(N):
            if tmp[i][j] == "Y" and i != j:
                cur_arr.append(j)
        arr[i] = cur_arr

    answer = []
    for i in range(N):
        friends = set()
        
        for ii in arr[i]:
            if ii != i:
                friends.add(ii)
                for iii in arr[ii]:
                    if iii != i:
                        friends.add(iii)
        
        answer.append(len(friends))
        
    print(max(answer))