import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    import sys
    from array import array
    input = sys.stdin.readline

    n, m = map(int, input().split())

    # 메모리 사용과 미세한 성능향상을 위한 array 자료형 사용
    arr = array('', map(int, input().split()))
    
    # {워킹 타임 : 사람 수}로 묶기
    time_dict = {}
    for i in arr:
        if i not in time_dict:
            time_dict[i] = 1
        else:
            time_dict[i] += 1

    # min_maximum, 이분 탐색의 최소한으로 둘 수 있는 최대값
    # 가장 적은 워킹타임 워커 하나로 m을 넘는 것을 최소한으로 가정
    mm = m * min(time_dict.keys())

    # top, bottom 설정
    t, b = mm, 1

    # 이분탐색
    while b <= t:
        c = (b + t)//2
        # current, k는 워킹타임, v는 워커 수
        cur = sum((c//k)*v for k,v in time_dict.items())
        
        if cur >= m:
            t = c - 1
        else:
            b = c + 1

    print(b)