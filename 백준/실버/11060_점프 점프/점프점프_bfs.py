import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n
    
    float('inf')

    def func():
        for i in range(n):
            # 가능한 범위를 탐색.
            for ii in range(i+1, i+1+arr[i]):
                # 왼쪽 끝이 아닌데 시작 지점이 0인 경우, 이전에 도착할 수 없었던 곳이므로 -1 반환
                # 이 코드가 가장 먼저 와야 정확한 탈출 지점을 찾아냄.
                if i > 0 and dp[i] == 0:
                    return -1
                # 만약 마지막 위치 이상으로 도달했다면 끝
                if ii >= n:
                    return max(dp)
                # 현재 위치에 처음 도달했을 경우
                if not dp[ii]:
                    # 시작지점의 dp 카운트 + 1을 현재 위치에 저장
                    dp[ii] = dp[i] + 1
    
    if n == 1:
        print(0)
    else:
        print(func())