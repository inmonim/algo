import os, sys

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys

input = sys.stdin.readline

c_list = ['D','S','L','R']

for _ in range(int(input())):
    
    n, T = map(int, input().split())
    
    check = {n:0}
    
    next_list = [['', n]]
    while next_list:
        
        body = next_list.pop(0)
        
        n = body[1]
        h = body[0]
        n1 = (n*2) % 10000
        n2 = n - 1
        if n2 == -1:
            n2 = 9999
        n3 = int(str(n)[1:] + str(n)[0])
        n4 = int(str(n)[-1] + str(n)[1:])
        
        n_list = [n1,n2,n3,n4]
        
        for i in range(4):
            n = n_list[i]
            h1 = h+c_list[i]
            
            if n == T:
                print(h1)
                next_list = []
                break
            elif n not in check:
                check[n] = 0
                next_list.append([h1, n])