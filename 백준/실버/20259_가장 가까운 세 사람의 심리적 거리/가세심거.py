import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

dist : dict = {}

def distance(x):
    for a in ['E', 'I']:
        for b in ['S', 'N']:
            for c in ['F', 'T']:
                for d in ['P', 'J']:
                    dis = 0
                    for i in range(4):
                        if x[i] != [a,b,c,d][i]:
                            dis += 1
                    dist[x][a+b+c+d] = dis

for a in ['E', 'I']:
    for b in ['S', 'N']:
        for c in ['F', 'T']:
            for d in ['P', 'J']:
                x = a+b+c+d
                dist[x] = {}
                distance(x)

@stdin_time
def sol(input):
    
    for T in range(int(input())):
        N = int(input())
        arr = input().strip().split()
        mbti = {}
        ans = 8
        p = 0
        for m in arr:
            mbti[m] = mbti[m]+1 if m in mbti else 1
        if p:
            continue
        for k, v in mbti.items():
            m = 8
            if v >= 3:
                ans = 0
                break
            elif v == 2:
                for dis_k, dis_v in dist[k].items():
                    if dis_k in mbti and k != dis_k:
                        m = min(m, dis_v*2)
            else:
                mbti_keys = list(mbti.keys())
                for i in range(len(mbti_keys)-1):
                    if k == mbti_keys[i]:
                        continue
                    for j in range(i+1, len(mbti_keys)):
                        if k == mbti_keys[j]:
                            continue
                        tmp = 0
                        tmp += dist[k][mbti_keys[i]]
                        tmp += dist[k][mbti_keys[j]]
                        tmp += dist[mbti_keys[i]][mbti_keys[j]]
                        m = min(tmp, m)
            ans = min(ans, m)
        
        print(ans)