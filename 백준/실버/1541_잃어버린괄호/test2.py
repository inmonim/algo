import os
import sys

sys.stdin =  open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys

input = sys.stdin.readline

N = input()
a, *b = [sum(map(int, i.split('+'))) for i in N.split('-')]

print(a, b)