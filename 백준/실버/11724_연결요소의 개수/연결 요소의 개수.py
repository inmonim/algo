import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    N, M = map(int, input().split())

    node = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        
        # 시작-도착, 도착-시작, 두 쌍 모두 node에 기록
        node[s].append(e)
        node[e].append(s)

    # 연결 요소가 아예 없는 고립된 경우도 연결 요소래요.
    # 비어있는 노드는 카운트 1 증가, node 리스트는 0번째 칸을 더미로 두고 있으므로 -1
    cnt = sum([0 if x else 1 for x in node])-1

    for i in range(len(node)):
        # 만약 해당 인덱스 노드에 값이 있을 경우 순회 시작
        if len(node[i]) >= 1:
            
            # stack에 해당 노드 값 넣어두고 stack 바닥날 때까지 순회
            stack = node[i]
            while stack:
                # 다음 노드는 스택에서 추출
                next_node = stack.pop()
                
                # 다음 노드에 값이 남아있을 경우 스택에 추가하고 해당 노드 초기화
                if node[next_node]:
                    stack.extend(node[next_node])
                    node[next_node] = []
                    
            # 스택이 바닥나면 한 개의 연결요소를 모두 순회한 것이므로 카운트 증가
            cnt += 1
    print(cnt)