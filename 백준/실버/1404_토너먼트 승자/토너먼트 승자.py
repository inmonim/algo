import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time
from pprint import pprint

@stdin_time
def sol(input):
    # 진짜 역대급 빡친 문제
    # 안 풀리는 게 아니라 너무 귀찮아!!!!
    
    arr = list(map(int, input().split()))
    # 서로에 대한 승률을 모두 저장할 dict list
    mat = [{} for _ in range(8)]
    
    # 각 라운드 별 승률을 저장
    first = {i : 0 for i in range(8)}
    second, third = first.copy(), first.copy()
    s = 0
    
    # 이 코드만 1시간 짠듯...
    # 8명의 각각 승률을 찾아야하므로 8번 순회
    for i in range(8):
        # 자신 제외 7명과 싸우므로, 최대 7번 순회
        for ii in range(i, 7):
            # 자신의 상대방에 대한 승률은 주어진 리스트 상, 다음과 같이 구한다.
            mat[i][ii+1] = arr[s + (ii-i)]/100
        
        # 자신보다 이전에 등장한 놈들과의 승률을 구해야함.
        ts = 0
        for ij in range(i):
            # 2차 시작 인덱스(ts) + 자신의 인덱스 - (대상의 인덱스 + 1)
            mat[i][ij] = (100 - arr[ts+(i-(ij+1))])/100
            # 2차 시작 인덱스 전진
            ts = ts + (7-ij)
        
        # 탐색을 시작해야하는 인덱스는 7 - i를 더하며 누적합
        s = s + (7-i)

    # 1라운드에서 최종적으로 몇 퍼센트로 이길 수 있는지 저장
    # 자신 + 1과의 승률을 저장해주자.
    for i in range(4):
        first[2*i] = mat[2*i][2*i+1]
        first[2*i+1] = mat[2*i+1][2*i]

    # 2라운드에서 최종적으로 몇 퍼센트로 이기는지 저장 (사실상 결승 진출 확률)
    # for i in range(4):
    #     # [0, 1], [4, 5]
    #     if i in [0, 2]:
    #         # x의 결승 진출 확률 = x의 2라운드 진출 확률 * (A가 2라운드에 진출할 확률 * x가 A를 이길 확률 + B가 2라운드에 진출할 확률 * x가 B를 이길 확률)
    #         second[2*i] = first[2*i] * (first[2*(i+1)] * mat[2*i][2*(i+1)] + first[2*(i+1)+1] * mat[2*i][2*(i+1)+1])
    #         second[2*i+1] = first[2*i+1] * (first[2*(i+1)] * mat[2*i+1][2*(i+1)] + first[2*(i+1)+1] * mat[2*i+1][2*(i+1)+1])
    #     # [2, 3], [6, 7]
    #     else:
    #         second[2*i] = first[2*i] * (first[2*(i-1)] * mat[2*i][2*(i-1)] + first[2*(i-1)+1] * mat[2*i][2*(i-1)+1])
    #         second[2*i+1] = first[2*i+1] * (first[2*(i-1)] * mat[2*i+1][2*(i-1)] + first[2*(i-1)+1] * mat[2*i+1][2*(i-1)+1])
    
    for i in range(8):
        if i in [0, 1]:
            for ii in range(2, 4):
                second[i] += first[i] * first[ii] * mat[i][ii]
        elif i in [2, 3]:
            for ii in range(0, 2):
                second[i] += first[i] * first[ii] * mat[i][ii]
        elif i in [4, 5]:
            for ii in range(6, 8):
                second[i] += first[i] * first[ii] * mat[i][ii]
        elif i in [6, 7]:
            for ii in range(4, 6):
                second[i] += first[i] * first[ii] * mat[i][ii]
            

    # 최종적으로, 왼쪽 반에서 올라오면 오른쪽 반이랑 싸우고, 오른쪽 반에서 올라오면 왼쪽 반이랑 싸우므로
    for i in range(8):
        se = [4, 8] if i < 4 else [0, 4]
        
        for ii in range(se[0], se[1]):
            third[i] += second[i] * second[ii] * mat[i][ii]
        third[i] = round(third[i], 9)
    
    # 이진트리의 특성을 이용하면 높이에 따라 값을 계속 계산할 수 있는 계산기를 만들 수 있겠으나, 못해먹겠다...

    print(*third.values())