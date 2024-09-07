import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    A = [""] + list(input().rstrip())
    B = [""] + list(input().rstrip())
    LCS = [[""]*len(B) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                LCS[i][j] = LCS[i-1][j-1] + A[i]
            else:
                if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                    LCS[i][j] = LCS[i-1][j]
                else:
                    LCS[i][j] = LCS[i][j-1]

    result = LCS[-1][-1]
    print(len(result))
    print(result)