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
        except Exception as e:
            # 에러 발생 시 캡처된 출력과 에러 메시지를 출력
            sys.stdout = original_stdout  # 표준 출력을 복구
            print("중간 출력:")
            print(captured_output.getvalue())  # 캡처된 출력 내용
            print("\n에러 발생:", e.with_traceback())  # 에러 메시지
            return
        finally:
            # 표준 출력을 원래대로 복구
            sys.stdout = original_stdout
            
        end_time = time.time()
        
        # 캡처된 출력문 확인
        output = captured_output.getvalue().strip().split('\n')
        answer = [s.strip() for s in sys.stdin.readlines()]
        
        if len(output) != len(answer):
            print("정답의 개수가 다릅니다.")
        else:
            _f = 0
            for i in range(len(output)):
                if output[i] != answer[i]:
                    _f = 1
                    print(f"{i} - {output[i]} 틀림, 정답 : {answer[i]}")
            if not _f:
                print("정답입니다.")
        
        print('=' * 50)
        run_time = end_time - start_time
        print(f'\n실행시간: {int(run_time * 1000)}ms, {int(run_time * 1_000_000)}us\n')
        
    return wrapper()