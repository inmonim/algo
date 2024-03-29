import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    tri = []
    for i in range(n := int(input())):
        tri.append(list(map(int, input().split())))

    # 삼각형의 밑부분부터 순회
    for i in range(n-1, -1, -1):
        edge = tri[i]
        # 깊은 복사
        up_edge = tri[i-1][:]
        
        # 해당 단계의 값 순회
        for i2 in range(i+1):
            x = edge[i2]
            # 윗 단계의 값 순회
            for j in range(i2-1, i2+1):
                if j == -1 or j == i:
                    continue
                
                # 깊은 복사가 이루어지지 않으면 up_edge가
                # tri의 바뀐 값을 실시간으로 따라감
                y = up_edge[j]
                s = x + y
                
                if tri[i-1][j] < s:
                    tri[i-1][j] = s

    print(tri[0][0])