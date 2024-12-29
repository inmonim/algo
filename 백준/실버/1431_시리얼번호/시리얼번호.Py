import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    
    serial = [input().strip() for _ in range(int(input()))]

    serial.sort(key=lambda x : (len(x), sum([int(i) for i in x if i.isdigit()]), x))

    print(*serial, sep='\n')