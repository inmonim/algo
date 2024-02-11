import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    ind = [1, 2, 3]
    house = []
    for _ in range(int(input())):
        rgb = list(map(int, input().split()))
        house.append(sorted(list(zip(rgb, ind))))
    last = 4
    ans = 0
    for h in house:
        for rgb in h:
            if rgb[1] != last:
                last = rgb[1]
                ans += rgb[0]
                break
    print(ans)