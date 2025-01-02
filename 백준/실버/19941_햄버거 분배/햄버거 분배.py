import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n, m = map(int, input().split())
    arr = list(input().strip())
    answer = 0
    for i in range(len(arr)):
        if arr[i] != "P":
            continue
        
        for ii in range(-m, m+1):
            if 0 <= i+ii < n and arr[i+ii] == "H":
                answer += 1
                arr[i+ii] = "X"
                break

    print(answer)