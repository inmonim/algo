import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

# 각 파티에서 만나는 사람들 간 루트를 그려서 연관관계를 만들고

# 연관관계 내부에 진실을 아는 사람이 있으면 해당 관계에 속한 사람이 존재하는 파티에 참석한 사람 모두가 진실을 알게 됨

# 진실을 모르는 사람들만 있는 연관관계에 속한 사람들만 있는 파티에서 얘기를 할 수 있다.


@stdin_time
def sol(input):
    N, M = map(int, input().split())
    trues = list(map(int, input().split()))
    true_p = []
    if trues[0] >= 1:
        true_p = trues[1:]
    else:
        print(M)
    
    partys = [list(map(int, input().split()))[1:] for _ in range(M)]
    
    insfested = [0]*(N+1)
    for p in true_p:
        insfested[p] = 1
    
    Q = true_p
    while Q:
        p = Q.pop(0)
        
        for party in partys:
            if p in party:
                for i in party:
                    if not insfested[i]:
                        Q.append(i)
                        insfested[i] = 1
    cnt = 0
    for party in partys:
        for p in party:
            if insfested[p]:
                break
        else:
            cnt += 1
            
    print(cnt)