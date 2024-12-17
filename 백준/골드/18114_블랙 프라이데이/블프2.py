import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    
    # 최대 3개 조합으로 m을 맞춰야 한다.
    # a는 arr[0], c는 arr[-1]로 시작한다.
    # a + c = m이라면 답이지만, m을 초과하면 c 인덱스를 1씩 줄인다.
    # m 미만이라면 b를 이분탐색으로 구한다.
    # 그럼에도 값이 없다면, a의 인덱스를 전진시킨다.

    def bs(b, t, target):
        while b <= t:
            mid = (b+t) // 2
            if arr[mid] > target:
                t = mid - 1
            elif arr[mid] < target:
                b = mid + 1
            else:
                return 1
        return 0

    def two_point(i, j):
        while i < j:
            a, c = arr[i], arr[j]
            if a + c == m:
                return 1
            elif a + c > m:
                j -= 1
            else:
                b = m - (a + c)
                if b not in [a, c] and bs(i, j, b):
                    return 1
                i += 1
                
        return 0
    
    i, j = 0, n-1
    
    if m in arr:
        print(1)
    else:
        print(two_point(i, j))