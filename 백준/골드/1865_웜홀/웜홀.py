import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

# 점들은 왕복 간선과 일방통행 웜홀로 연결되어있다.

# 간선은 지날 때마다 주어진 시간이 흐르고, 웜홀은 주어진 시간을 역행할 수 있다.

# 어떤 점에서 시작하여 자유롭게 돌아다닌 뒤, 시작 지점으로 돌아왔을 때, 시간이 오히려 줄어든 경우가 있을지 찾아내자.

# 정확한 수치가 아닌, 가능 여부만 알아내면 되는 것이다!

# 특정 시작 위치가 정해지는 것이 아니라, 모든 점에서 시작하고 끝이 가능하다!

# 시작 지점 A가 있고, 웜홀의 시작 X와 웜홀 끝 Y가 있다고 하자.

# A에서 X로 간 뒤, Y에서 A로 돌아가는 거리의 합이 웜홀의 역행 시간보다 작다면 된다.

# 그런데, X에서 웜홀을 타고 Y로 가서 역행한 시간이, Y에서 다시 X로 가는 시간보다 크다면?

# Y에서 A로 가는 것만 가능하면 사실상 무조건 YES가 된다..!

# 1. 시작 지점에서 웜홀의 시작 지점으로 간다.

# 2. 웜홀을 탄다.

# 3. 웜홀 끝지점에서...

# 그냥 다익스트라 돌리면 되지 않나?

@stdin_time
def sol(input):

    TC = int(input())

    for _ in range(TC):
        N, M, W = map(int, input().split())
        
        node = [[] for _ in range(N+1)]
        
        for i in range(M+W):
            S, E, T = map(int, input().split())
            if i >= M:
                T = -T
            else:
                node[E].append((T, S))
            node[S].append((T, E))
            
        dist = [0] * (N+1)
        
        def b_f():
            for i in range(N):
                for j in range(1, N+1):
                    for n_node in node[j]:
                        nv, ni = n_node
                        rv = nv + dist[j]
                        if dist[ni] > rv:
                            dist[ni] = rv
                            if i == N-1:
                                return 'YES'
            return 'NO'
        
        print(b_f())