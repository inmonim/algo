import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):

    x=[sum(map(int,x.split('+')))for x in input().split('-')]
    print(x[0]-sum(x[1:]))