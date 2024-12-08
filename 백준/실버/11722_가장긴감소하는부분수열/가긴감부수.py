
import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time
from pprint import pprint

@stdin_time
def sol(input):
    l = int(input())
    arr = list(map(int, input().split()))

    answer = [[[arr[0]] for _ in range(l)] for _ in range(l)]
    for i in range(1, l):
        for j in range(l):
            
            # 탐색하려는 숫자의 자리이거나, 그 뒤인 경우
            if j >= i:
                # 만약 이전에 저장한 값의 시작이 탐색하려는 숫자보다 작다면, 탐색하는 숫자 시작으로 초기화
                if answer[i-1][j][0] < arr[i]:
                    answer[i][j] = [arr[i]]
                # 아니라면 이전 값을 계승하여 가져오기
                else:
                    answer[i][j] = answer[i-1][j]
            
            # 탐색하는 숫자의 자리보다 앞일 경우
            else:
                # 탐색하는 숫자보다, 저장된 값의 마지막이 크다면, 저장된 값 + 탐색하는 숫자
                if answer[i-1][j][-1] > arr[i]:
                    answer[i][j] = answer[i-1][j] + [arr[i]]
                # 아니라면 이전 값을 계승하여 가져옴
                else:
                    answer[i][j] = answer[i-1][j]
    
    pprint(answer)
    res = 0
    for a in answer[-1]:
        res = max(res, len(a))

    print(res)