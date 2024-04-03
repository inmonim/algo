import sys, os, time

def stdin_time(func):
    
    def wrapper():
        
        # 파일의 절대 경로 파악
        executing_file = sys.argv[0]
        
        # 절대 경로에 등록된 input 파일 open
        sys.stdin = open(os.path.dirname(executing_file)+'/input.txt')
        input = sys.stdin.readline
        
        print('='*50)
        start_time = time.time()
        func(input)
        end_time = time.time()
        print('='*50)
        run_time = end_time - start_time
        print(f'\n실행시간: {int(run_time*1000)}ms\n')
        
    return wrapper()