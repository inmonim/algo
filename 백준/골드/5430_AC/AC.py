import os, sys

sys.stdin = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt')

# 선영이는 할 짓이 없어서 AC라는 언어를 만들었다고 한다.

# 커도 반 센세인가?

# 정수 배열을 연산하기 위한 언어로, 두 가지 함수가 존재한다.

# R(뒤집기)는 배열의 수를 뒤집는 것, D(드랍)은 del List[0]이다.

# 배열이 비어있을 때 D를 사용하면 에러가 발생한다. 함수가 두 개 밖에 없는데 예외 처리가 고작 에러다.

# 배열의 초기값과 수행 함수가 주어졌을 때, 최종 결과를 구하라.

# 문제 자체는 어렵지 않은데, 극한의 국어 문제다. 문제가 무슨 유희왕 몬스터 카드 효과마냥 꼬여있다.

# 일단 입력 자체가 괴랄한데,

# 첫 번째로 테스트 케이스의 수 T 온다. 이건 백준 문제에서는 많이 등장하지 않는 유형이고,

# 삼성 sw 아카데미 문제 출제 형식인데, 하나의 완성된 테스트 케이스 세트가 여러 개 들어온다는 뜻이다.

# 그리고 해당 테스트 케이스에 쓰일 함수 p가 문장으로 입력된다.

# 다음으로 테스트 케이스에서 쓰일 초기 배열의 길이 n을 받는다.

# 그 다음에 해당 테스트 케이스의 초기 배열을 리스트 형식의 문자열로 입력받는다. (즉, 문자열을 파싱하거나 eval함수로 바꾸어줘야 한다)

# 출력은 error 또는 리스트인데, 이 리스트 조차도 문자열로 출력해야한다...

# 골드 5 문제 치고 평균 정답 비율이 20퍼센트라는 괴멸적인 수준을 보이는데, 국어문제라서 그런 걸까...?



import sys

input = sys.stdin.readline

for t in range(int(input())):
    func = input().strip().replace('RR','').split('R')
    rev = 0
    if len(func) > 1 and len(func)%2 == 0:
        rev = 1
 
    l = int(input())
    arr = []
    arr_string = input().strip()
    string = ''
    if l:
        arr = arr_string[1:-1].split(',')
    p, r = 0, 0
    for i in range(len(func)):
        if i%2 == 0:
            p += len(func[i])
        else:
            r += len(func[i])
        if p+r > l:
            print('error')
            break
    
    else:
        if r:
            arr = arr[p: -r]
        else:
            arr = arr[p:]
        if rev:
            arr.reverse()
        print(f"[{','.join(arr)}]")