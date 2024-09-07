import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    
    MOD = 1000000

    # 2x2 행렬 곱셈 함수
    def matrix_mult(A, B):
        return [
            [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
        ]

    # 행렬의 거듭제곱 함수
    def matrix_pow(M, exp):
        result = [[1, 0], [0, 1]]  # 단위 행렬
        base = M

        while exp > 0:
            if exp % 2 == 1:
                result = matrix_mult(result, base)
            base = matrix_mult(base, base)
            exp //= 2

        return result

    # n번째 피보나치 수를 구하는 함수
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # 기본 피보나치 행렬
        F = [[1, 1], [1, 0]]
        
        # F^(n-1) 구하기
        result_matrix = matrix_pow(F, n-1)
        
        # F(n) = result_matrix[0][0]
        return result_matrix[0][0]

    # 입력 받기
    n = int(input().strip())

    # 결과 출력
    print(fibonacci(n))