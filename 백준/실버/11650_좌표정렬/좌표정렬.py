
import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    # input으로 들어오는 모든 값을 한 번에 읽기. n은 사실 필요 없으니 건너뛴다.
    xy = sys.stdin.readlines()[1:]

    # 값의 범위는 -100,000 ~ 100,000 이다.
    # 그러므로 x를 임계값인 200,001로 곱하고, y를 더하면
    # 각 행이 모두 독립적인 값을 가지게 되며
    # 정렬했을 때, 문제에서 요구하는 "x가 같으면 y를 기준으로 오름차순 정렬"에 맞게 정렬할 수 있다.
    xy.sort(key=lambda a: int(a.split()[0])*200_001+int(a.split()[1]))

    # 또한 strip()을 통해 '\n'을 지우지 않았으므로
    # 한 줄의 프린트로 자동으로 개행이 진행된다.
    print(''.join(xy))