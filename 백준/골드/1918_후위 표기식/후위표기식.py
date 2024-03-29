import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

# 일반적인 중위 표기식 입력이 들어오면

# 후위 표기식으로 바꿔 출력하면 끝이다.

# 입력은 사칙 연산 부호와 알파벳만 들어온다

@stdin_time
def sol(input):
    
    S = input()

    stack = []
    result = ''

    for i in S:
        if i.isalpha():
            result += i
        else:
            if not stack:
                stack.append(i)
            elif i == '(':
                stack.append(i)
            elif i in '/*':
                while stack and stack[-1] in '/*':
                    result += stack.pop()
                stack.append(i)
            elif i in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    while stack:
        result += stack.pop()
    
    print(result)