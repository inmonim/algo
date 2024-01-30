def stdin_time(func):
    def wrapper():
        import sys, os, time
        executing_file = sys.argv[0]
        
        sys.stdin = open(os.path.dirname(executing_file)+'/input.txt')
        input = sys.stdin.readline
        
        print('='*50)
        start_time = time.time()
        func(input)
        end_time = time.time()
        print('='*50)
        run_time = end_time - start_time
        print(f'\n실행시간: {int(run_time*1000)}ms\n')
        
    return wrapper