T = int(input())

def f(d, l, n):
    for i in range(n):
        if l[i] in d:
            d[l[i]] += 1
        else:
            d[l[i]] = 1
    return d

def bs(bdl, tar):
    b, t = 0, len(bdl) - 1
    
    while b <= t:
        m = (b + t) // 2
        if bdl[m] < tar:
            b = m + 1
        else:  # tar 이하일 때 t를 줄여서 작은 값 탐색
            t = m - 1
    
    return b

def sol_func():
    n, m = map(int, input().split())
    a, b = list(map(int, input().split())), list(map(int, input().split()))

    ad, bd = f({}, a, n), f({}, b, m)

    adl = sorted(list(ad.keys()), reverse=True)
    bdl = sorted(list(bd.keys()))
    
    # B의 누적합 계산
    ac = 0
    for k in bdl:
        ac += bd[k]
        bd[k] = ac

    answer = 0
    for x in adl:
        if x > bdl[-1]:  # x가 B의 최댓값보다 큰 경우
            answer += ad[x] * bd[bdl[-1]]
        elif x > bdl[0]:  # x가 B의 최솟값보다 클 경우
            y = bs(bdl, x)  # x보다 작은 값의 위치
            if y > 0:  # x보다 작은 값이 존재하면
                answer += ad[x] * bd[bdl[y - 1]]

    print(answer)

for _ in range(T):
    sol_func()