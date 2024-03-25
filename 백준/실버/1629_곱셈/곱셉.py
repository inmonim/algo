import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    a, b, c = map(int, input().split())
    
    def dac(a, b, c):
        
        if b == 1:
            return a % c
        elif not b % 2:
            return (dac(a, b//2, c) ** 2) % c
        else:
            return ((dac(a, b//2, c) ** 2) * a) % c
        
    print(dac(a,b,c))
    
    # print(pow(a,b,c))