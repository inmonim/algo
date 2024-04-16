import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    y = 1
    while n := int(input()):
        names = []
        x_l = []
        for i in range(n):
            name, *arr = input().split()
            names.append(name)
            for a in range(len(arr)):
                if arr[a] == 'N':
                    x_l.append((i, i-(a+1)))

        print(f'Group {y}')
        for x in x_l:
            i, a = x
            print(f'{names[a]} was nasty about {names[i]}')
        if not x_l:
            print("Nobody was nasty")
        print('')
        y += 1
            