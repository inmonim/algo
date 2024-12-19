import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n = int(input())

    xys = [list(map(int, input().split())) for _ in range(n)]
    qs = [float(input().strip()) for _ in range(int(input()))]

    # 이분 탐색 시~작!
    # lst[m] == tar 인 경우는 없음
    def bs(lst, tar):
        b, t = 0, len(lst) - 1
        while b <= t:
            m = (b + t) // 2
            if lst[m] < tar:
                b = m + 1
            else:
                t = m - 1
        return b

    # 0 : 0 을 넣어서 풀리지 않았다.
    # 0 : 0이 들어갈 경우, 최저값이 0으로 제대로 안 들어가는 경우가 있었음
    slop = { }

    # i-1 에서 i로 올 때, y가 증감량을 따져 slop에 저장
    for i in range(1, n):
        px, py = xys[i-1]
        x, y = xys[i]
        
        if py < y:
            slop[x] = 1
        elif py > y:
            slop[x] = -1
        else:
            slop[x] = 0

    # 키값을 list로 변환해서 정렬하기
    xs = sorted(list(slop.keys()))

    for q in qs:
        # 바이너리 썰치
        x = bs(xs, q)
        # 반환된 인덱스에 해당하는 x값을 slop 딕셔너리에서 찾기
        print(slop[xs[x]])