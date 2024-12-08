import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    n, m = map(int, input().split())

    time_dict = {}

    for i in list(map(int, input().split())):
        
        if i not in time_dict:
            time_dict[i] = 1
        else:
            time_dict[i] += 1

    time_list = sorted(list(time_dict.keys()))

    min_time = time_list[0]
    min_time_cnt = 1
    answer = 0
    while not answer:
        t = min_time * min_time_cnt
        
        cur_m = 0
        for k, v in time_dict.items():
            cur_m += (t//k)*v
        
        if cur_m >= m:
            answer = t
            
            t = min_time*(min_time_cnt - 1)
            
            while t < answer:
                cur_m = 0
                for k, v in time_dict.items():
                    cur_m += (t//k)*v
                if cur_m >= m:
                    answer = t
                    break
                else:
                    t += 1
        else:
            min_time_cnt += 1

    print(answer)