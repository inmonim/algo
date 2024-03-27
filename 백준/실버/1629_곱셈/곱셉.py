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
        mod = dac(a, b//2, c)
        if not b % 2:
            return (mod ** 2) % c
        else:
            return (mod ** 2) % c
        
    print(dac(a,b,c))
    
    # print(pow(a,b,c))
    
    # (A * B) mod C == ((A mod C) * (B mod C)) mod C
    
    # (a * mod ** 2) % c
    
    # (a * (a mod c)^2) mod c
    
    # =(a mod c * (a mod c)^2 mod c) mod c
    
    # =(a mod c * (a mod c * a mod c) mod c) mod c
    
    # =(a mod c * (a * a) mod c) mod c
    
    # =(a mod c * a^2 mod c) mod c
    
    # =(a * a^2) mod c
    
    # =a^3 mod c
    
    
    # (a%c * mod ** 2) % c
    
    # = (a mod c * (a mod c)^2) mod c
    # = (a mod c * a mod c * a mod c) mod c
    # = (a mod c)^3 mod c
    # = a^3 mod c