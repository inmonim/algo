import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    x = input()
    oper = ''
    am, bm = 0, 0
    for i in range(len(x)):
        if not x[i].isdigit():
            if i == 0:
                am = 1
            elif not oper:
                oper = x[i]
                a, b = x[:i], x[i+1:]
            elif oper:
                bm = 1

    a, b = -int('0o'+a[1:], 8) if am else int('0o'+a, 8), -int('0o'+b[1:], 8) if bm else int('0o'+b, 8)

    if oper == '+':
        r = a+b
    elif oper == '-':
        r = a-b
    elif oper == '*':
        r = a*b
    else:
        if b == 0:
            r = 'invalid'
        else:
            r = a//b

    if r == 'invalid':
        print(r)
    else:
        r = oct(r)
        if int(r, 8) < 0:
            print('-'+r[3:])
        else:
            print(r[2:])