import os
import sys

sys.stdin =  open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

import sys

input = sys.stdin.readline

N = input()+'e'

# 도대체 이게 뭔 코드야 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

a = 0
m = 0
n = ''
for i in N:
    if i.isdigit():
        n += i
    else:
        n = int(n)
        if not m:
            a += n
            if i == '-':
                m = 1
        else:
            a -= n
        n = ''
print(a)