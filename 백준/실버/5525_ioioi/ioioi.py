import os, sys

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')


# 최초 입력 N이 들어오면, N+1 개의 I와 N개의 O가 교차로 나오는 문자열을 PN이라 한다.

# 즉, IOI 는 P1, IOIOI는 P2를 의미한다.

# N과 문자열 S의 길이, 그리고 문자열 S가 들어왔을 때, S 안에는 Pn이 몇 개가 포함됐는지 출력한다.

# 딱 봐도 S의 0부터 순회하며 문자열을 일일히 검증하는 건 무조건 시간 초과가 생길 것 같은 문제다.

# replace를 활용해 무조건 건너 뛰는 문자열을 제거하는 것으로 시작한다.

# O가 두 번 이상 반복되면 삭제하고, I가 세 번 이상 반복되는 것은 II로 치환하면 될 것이다.

# 만약 N2이고 S는 IOIIIOIOI일 때, Pn은 1번 등장하지만, III를 I로 치환하거나 없앨 경우 2번 또는 0번으로 바뀌기 때문이다.

# 세 개 이상의 I를 2개로 바꾸면 이러한 문제들이 해결된다.

import sys

input = sys.stdin.readline

ioi = 'I'

N = int(input())
ioi += 'OI'*(N)
L = int(input())
S = input().strip()

ans = 0
l = len(ioi)
flag = 0

i = 0
while i < len(S):
    if flag:
        if S[i:i+2] == 'OI':
            ans += 1
            i += 2
        else:
            flag = 0
    else:
        i = S.find(ioi, i)
        if i == -1:
            break
        ans += 1
        i += l
        flag = 1

print(ans)

# 정규표현식으로 글자수를 줄일 필요가 없었고, 오히려 오버헤드가 발생했다.

# 처음에는 i를 +1씩 올리며 순회했는데, 그로 인해 엄청난 시간이 소모됐던 모양이다.

# S[i:i+l]로 슬라이싱하고 비교하여 일치 여부를 파악하는 것은

# .find(ioi) 메서드를 사용하는 것에 비해 굉장히 큰 오버헤드가 있었던 모양이다.

# GPT에 따르면, find 메서드는 내부적으로 C언어로 구현되어 있어

# 내가 python으로 구현한 find메서드와 동일한 기능을 하는 코드와는 성능면에서 압도적인 차이를 보일 수밖에 없다고 한다.