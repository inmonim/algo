import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    arr = [input(), input(), input()]

    tar = 0
    for i in range(3):
        if arr[i][0].isdigit():
            tar = int(arr[i]) + (3-i)
            break
    res = ''
    if not tar % 3:
        res += 'Fizz'
    if not tar % 5:
        res += 'Buzz'

    print(res) if res else print(tar)