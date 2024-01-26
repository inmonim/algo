import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__))+'/input.txt')


import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = [1, 1, 1, 2, 2, 3]
    T = int(input())
    while T > len(N):
        N.append(N[-1]+N[-5])
    print(N[T-1])
