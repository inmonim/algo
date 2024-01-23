import sys, os

sys.stdin = open(os.path.dirname(os.path.realpath(__file__))+'/input.txt')

# 이딴 달력을 쓰니까 망했지...라고 하기엔 우리나라도 비슷한 게 있다...

# M과 N보다 작거나 같은 자연수로 연도를 <x, y>와 같이 표현한다.

# 우리나가라 해의 이름을 정할 때와 같은 방식이다.

# 갑을병정... 등의 십간과 자축인묘... 등의 십이지신을 사용하는 방법이다.

# 2024년인 올해는 갑진년 청룡의 해다.

# 갑은 십간의 첫 번째, 진은 십이지신의 다섯 번째

# 이번 문제로 표현하면, <1, 5>가 되는 것이다.

# 값은 똑같이 증가하나, x는 M진법, y는 N진법을 쓴다고 보면 되겠다.

# 정확히는 1부터 시작하여 M과 N까지 이르는 방식이기 때문에 엄밀히 말하면 진법은 아니지만.

# 어쨌든 이 패턴에 따라 주어진 <x, y>는 <1, 1> 부터 몇 번째 해인지 알아내는 것 문제다.

# 만약 유효하지 않은 수라면 -1을 출력하면 된다.

# 수학 문제인 것 같다.

import sys

input = sys.stdin.readline

for t in range(int(input())):
    
    M, N, x, y = map(int, input().split())
        
    n = x
    while n <= M*N:
        if n%N == y or (N == y and n%N == 0):
            print(n)
            break
        n += M
        
    else:
        print(-1)