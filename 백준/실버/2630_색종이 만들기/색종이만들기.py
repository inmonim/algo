import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt")

# 1과 0으로 이루어진, 길이가 똑같은 2차원 배열이 들어온다.

# N/2 길이의 2차원 배열로 내부를 나눌 때, 나눈 배열 안이 한 가지 수로만 이루어져 있으면

# 해당 색깔 (1: 파랑, 0: 하양) 색종이가 완성된 것으로 친다.

# 모든 부분을 나누었을 때, 각각 완성된 색종이는 몇 개인가?

import sys

input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

def graph(n, m, paper):
    global b, w
    for dx, dy in [(0, 0), (0, n), (n, 0), (n, n)]:
        check = 0
        for y in range(dy, dy+n):
            check += sum(paper[y][dx : dx+n])
        if check == m:
            b += 1
        elif check == 0:
            w += 1
        else:
            graph(n//2, m//4, [paper[y][dx : dx+n] for y in range(dy, dy+n)])

f = sum([sum(p) for p in paper])

if f == N**2:
    print(f'{0}\n{1}')
elif not f:
    print(f'{1}\n{0}')
else:
    n = N//2
    m = N**2 // 4
    b,w = 0,0
    graph(n, m, paper)
    print(f'{w}\n{b}')