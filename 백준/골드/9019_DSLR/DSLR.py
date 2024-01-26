import os, sys

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    
    n, T = map(int, input().split())
    Q = deque()
    head = {n:''}
    
    Q.append(n)
    while Q:
        
        n = Q.popleft()
        h = head[n]
        
        if n == T:
            print(h)

        n1 = (n*2) % 10000
        if n1 not in head:
            h1 = h+'D'
            head[n1] = h1
            Q.append(n1)
            
        n2 = (n-1) % 10000
        if n2 not in head:
            h2 = h+'S'
            head[n2] = h2
            Q.append(n2)
            
        n3 = ((n%1000)*10+(n//1000))
        if n3 not in head:
            h3 = h+'L'
            head[n3] = h3
            Q.append(n3)

        n4 = ((n%10)*1000)+(n//10)
        if n4 not in head:
            h4 = h+'R'
            head[n4] = h4
            Q.append(n4)
