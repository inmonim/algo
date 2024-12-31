import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    # 푸는 데 10분
    # ceil, floor 헷갈려서 12분 추가
    n, m = int(input()), int(input())
    arr = list(map(int, input().split()))
    import math
    
    # 왼쪽, 오른쪽 끝은 가장 가까운 가로등과의 거리만큼 높이가 필요함.
    # 중간에 위치한 가로등들은, (다음(오른쪽)에 위치한 가로등 위치 - 이전(왼쪽)에 위치한 가로등 위치) 한 다음
    # 2로 나누고, 겹치는 부분이 생기더라도 비는 부분이 생기면 안 되므로 ceil을 통해 정수로 올림해줘야 함.
    
    ns = [math.ceil((arr[i] - arr[i-1]) / 2) for i in range(1, m)] + [arr[0], n - arr[-1]]
    print(max(ns))