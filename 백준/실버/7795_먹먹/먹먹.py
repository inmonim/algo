import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    T = int(input())

    # 딕셔너리에 {크기 : 수}를 넣고, 중복 제거한 크기 리스트를 반환
    def f(d, l, n):
        keys = []
        for i in range(n):
            if l[i] in d:
                d[l[i]] += 1
            else:
                d[l[i]] = 1
                keys.append(l[i])
        return d, sorted(keys)

    def bs(bdl, tar):
        """
        idx : 0 1 2 3 4 
        먹이 : 2 4 6 8 10
        포식 :  3
        """
        b, t = 0, len(bdl) - 1
        while b <= t:
            m = (b + t) // 2
            if bdl[m] < tar:
                b = m + 1
            else:
                t = m - 1
        return b
        
    def sol_func():
        n, m = map(int, input().split())
        a, b = list(map(int, input().split())), list(map(int, input().split()))

        ad, adl = f({}, a, n)
        bd, bdl = f({}, b, m)

        # 누적값으로 딕셔너리를 업데이트
        # bd[n]에는 bd[0] + bd[1] ... bd[n] 의 값이 할당됨
        ac = 0
        for k in bdl:
            ac += bd[k]
            bd[k] = ac

        answer = 0
        for x in adl:
            # 포식자가 먹이의 가장 큰 크기보다 클 경우 (포식자 수 * 모든 먹이) 더하기
            if x > bdl[-1]:
                answer += ad[x] * bd[bdl[-1]]
            # 가장 작은 먹이 보다 포식자가 큰 경우
            elif x > bdl[0]:
                y = bs(bdl, x)
                # 먹이의 크기가 포식자와 같거나, 한 사이즈 큰 idx를 반환하므로 -1
                answer += ad[x] * bd[bdl[y-1]]
                
        print(answer)

    for _ in range(T):
        sol_func()