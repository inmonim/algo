import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    import array

    n = int(input())
    arr = array.array('i')

    for _ in range(n):
        arr.extend(list(map(int, input().split())))
    arr2 = arr.__copy__()

    def find_m(route, func, mv):
        i = 1
        while i < n:
            for j in range(3):
                m = mv
                for k in range(-1, 2):
                    if 0 <= j + k < 3:
                        m = func(m, route[(i-1)*3+(j+k)] + route[i*3+j])
                route[(i*3)+j] = m
            i += 1
        print(func(route[-3:]), end=' ')

    find_m(arr, max, 0)
    find_m(arr2, min, n*10)