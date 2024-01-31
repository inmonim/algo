import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys

input = sys.stdin.readline


for _ in range(int(input())):
    
    n = int(input())
    a = [0, 1, 2, 4]
    while len(a) <= n:
        a.append(a[-3] + a[-2] + a[-1])
    
    print(a[n])