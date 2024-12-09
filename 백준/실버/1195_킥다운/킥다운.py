import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    a, b = list(map(int, list(input().strip()))), list(map(int, list(input().strip())))

    # 최악의 최대값은 두 기어의 길이를 더한 것
    answer = len(a) + len(b)

    # 첫 번째 기어의 왼쪽과 두 번째 기어의 오른쪽을 맞추어 진행
    for i in range(-len(b), len(a)-1, 1):
        
        for ii in range(len(b)):
            
            # 겹치는 부분인데, 2 + 2 인 경우 탈출!
            if (len(a) > i+ii >= 0) and (a[i+ii] + b[ii] > 3):
                break
        # 탈출하지 않고 정상적으로 순회가 완료되는 경우 실행되는 코드
        else:
            # 길이 찾기
            tmp = max(len(a), i + len(b)) - min(0, i)
            answer = min(answer, tmp)

    print(answer)