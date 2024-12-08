import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N = int(input())

    arr = [input().strip() for _ in range(N)]

    answer = 0
    for i in range(N):
        friends = set()
        
        for ii in range(N):
            if arr[i][ii] == 'Y' and i != ii:
                friends.add(ii)
                
                for iii in range(N):
                    if arr[ii][iii] == 'Y' and i != iii:
                        friends.add(iii)
        
        answer = max([answer, len(friends)])

    print(answer)