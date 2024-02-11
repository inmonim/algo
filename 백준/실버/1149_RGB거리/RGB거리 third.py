import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

# n*3번째 칸에서 계산한다.

# 3번째 칸에서 R을 선택하기 위해선, R-G-R, R-B-R, B-G-R, G-B-R 이렇게 네 개의 방법이 있으며,

# 마찬가지로 3번째 칸에서 G, B를 선택하는 경우도 4개 씩, 총 12개가 생긴다.

# 중요한 것은 이렇게 각 칸에 도달하는 각 4개의 경우 중 가장 작은 값을 스택에 저장한 후,

# 다시 위의 계산을 반복하면 되는 것이다.

@stdin_time
def sol(input):
    N = int(input())
    rgb = [list(map(int, input().split())) for _ in range(N)]
    order1 = ((0,2,0),(0,1,0),(1,2,0),(2,1,0))
    order2 = ((1,2,1),(1,0,1),(0,2,1),(2,0,1))
    order3 = ((0,1,2),(1,0,2),(2,0,2),(2,1,2))
    
    f, s, t = rgb[0]
    n = 3
    for x in range(1, N//2+1):
        if x == N//2 and not N%2:
            n = 2
        arr = [[f,s,t]] + rgb[x*2-1:x*2+1]
        f_l, s_l, t_l = [], [], []
        for i in range(4):
            f, s, t = 0, 0, 0
            for j in range(n):
                f += arr[j][order1[i][j]]
                s += arr[j][order2[i][j]]
                t += arr[j][order3[i][j]]
            f_l.append(f)
            s_l.append(s)
            t_l.append(t)
        f, s, t = min(f_l), min(s_l), min(t_l)  
    
    print(min([f,s,t]))