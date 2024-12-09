import sys
import os
import time
import io

def stdin_time(func):
    def wrapper():
        
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        sys.path.append(path)
        # 파일의 절대 경로 파악
        executing_file = sys.argv[0]

        # 절대 경로에 등록된 input 파일 open
        sys.stdin = open(os.path.dirname(executing_file) + '/input.txt')
        input = sys.stdin.readline
        
        print('=' * 50)
        start_time = time.time()

        try:
            # 표준 출력을 리다이렉트
            original_stdout = sys.stdout
            captured_output = io.StringIO()
            sys.stdout = captured_output
            func(input)
            sys.stdout = original_stdout
            print(captured_output.getvalue().strip())

        finally:
            # 표준 출력을 원래대로 복구
            sys.stdout = original_stdout

        # 캡처된 출력문 확인
        output = captured_output.getvalue().strip()
        answer = input().strip()
        
        if not answer:
            print("input에 정답 값은 없는 것 같습니다.")
        elif output != answer:
            print("\n틀렸습니덩, 정답은 : ", answer)
        elif output == answer:
            print("\n정답입니덩!")
        
        end_time = time.time()
        print('=' * 50)
        run_time = end_time - start_time
        print(f'\n실행시간: {int(run_time * 1000)}ms, {int(run_time * 1_000_000)}us\n')
        
    return wrapper()