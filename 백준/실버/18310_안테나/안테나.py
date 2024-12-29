import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    
    n = int(input())
    x = list(map(int, input().split()))
    # arr을 주어진 집 주소 중 가장 큰 값만큼 생성
    arr = [0] * max(x)

    # arr의 주소마다 주택의 수를 카운트
    for i in x:
        arr[i-1] += 1

    # 0을 기준으로 왼쪽, 오른쪽에 위치한 집의 개수 카운트
    lc, rc = 0, sum(arr[1:])
    # 0을 기준으로 왼쪽, 오른쪽에 위치한 집의 총 거리를 계산
    ls, rs = 0, sum([abs(0 - i) * arr[0] for i in range(len(arr))])

    # 현재 최대값
    ms = ls+rs
    answer = 0
    for i in range(1, len(arr)):
        # 안테나 위치 왼쪽에 집이 있는 경우, 왼쪽 집 카운트 올려주기
        if arr[i-1]:
            lc += arr[i-1]
        # 안테나 현재 위치에 집이 있는 경우, 오른쪽 집 카운트 내리기
        if arr[i]:
            rc -= arr[i]
        # 왼쪽 집의 개수만큼 거리가 멀어졌으므로 합산
        ls += lc
        # 오른쪽으로 전진 중이므로, 오른쪽 집 카운트만큼 거리 내리기
        rs -= (arr[i] + rc)
        # 현재까지 거리 총합의 최소 값보다 작아진 경우 갱신
        if ms > ls+rs:
            ms = ls+rs
            answer = i
        # 거리 총합은 최저점 이후 반드시 증가만 하므로, 만약 증가할 경우 끝.
        elif ms < ls+rs:
            break

    print(answer+1)