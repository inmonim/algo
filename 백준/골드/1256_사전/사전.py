import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    from math import comb
    
    from itertools import permutations, combinations
    
    x = '12345'
    y = 'azz'
    
    print(comb(5, 3))
    

    def find_kth_string(N, M, K):
        # 전체 조합이 K보다 작다면 -1 반환
        total_combinations = comb(N + M, N)
        if K > total_combinations:
            return -1

        result = []
        while N > 0 and M > 0:
            # 'a'를 선택했을 때 가능한 조합의 수
            # 첫 위치에 a를 넣고, 나머지 N + M - 1 개의 자리에 N - 1 개의 a를 배치하는 경우의 수
            a_combinations = comb(N + M - 1, N - 1)
            
            # string = 'aaazz', N = 3, M = 2
            # comb(N+M, N) : 가능한 모든 조합의 수, N+M만큼의 리스트에 N개의 값을 서로 다른 위치에 삽입하는 경우의 수를 구한다 보면 됨
            # comb(N+M-1, N-1) : 4개 중 2개를 선택하여 조합, a 하나를 가장 앞에 두었다고 가정, aazz로 나눠서 경우의 수를 구함. 경우의 수는 6이 나옴
            # comb(N+M-1, M-1) : 4개 중 1개를 선택하여 조합, z 하나를 가장 앞에 두었다고 가정, aaaz로 나누어 경우의 수를 구함. 경우의 수는 4가 나옴
            # 즉, comb(N+M-1, N-1) + comb(N+M-1, M-1) = 10이 됨.
            # 여기서 k가 속할 수 있는 값의 범위는 다음과 같음
            # 0 <= k <= comb(N+M-1, N-1):6, < k <= comb(N+M, N):10
            # 사전순서로 배열하므로, comb(N+M-1, N-1)의 범위에 해당하는 값이 먼저 등장하고, 그 이후로 comb(N+M, N):10 범위 경우가 등장함.
            # 즉, k가 6이하라면 가장 앞 자리에 a가 온 경우에 해당하며,
            # k가 6초과 10이하라면 가장 앞 자리에 z가 온 경우에 해당하게 되는 것임.
            
            # K는 0이상 현재의 N+M, N 의 전체 조합 수 이하임.
            # 따라서 k가 a_comb 이하인 경우, a가 가장 앞에 오며
            # 초과일 경우 z가 가장 앞에 오게 됨
            if K <= a_combinations:
                # K가 'a'로 시작하는 범위에 속하면 'a'를 선택
                result.append('a')
                N -= 1
            else:
                # 그렇지 않으면 'z'를 선택하고 K값을 감소
                result.append('z')
                M -= 1
                K -= a_combinations

        # 남은 'a' 또는 'z'를 결과에 추가
        result.extend(['a'] * N)
        result.extend(['z'] * M)

        return ''.join(result)

    # 입력 예제
    N,M,K = map(int, input().split())
    print(find_kth_string(N, M, K))