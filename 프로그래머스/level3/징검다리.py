def solution(stones, k):
    answer = 0
    
    # {가능회수 : [위치들]}로 일단 만듦
    cnt_idxs = {}
    for i in range(len(stones)):
        if cnt_idxs.get(stones[i]):
            cnt_idxs[stones[i]].append(i)
        else:
            cnt_idxs[stones[i]] = [i]
    
    # 가능회수를 리스트로 오름차순 정렬
    cnt_list = sorted(list(cnt_idxs.keys()))
    
    # 죽은 징검다리를 set으로 모아둠
    dead_set = set()
    
    # 가능회수를 순회
    for c in cnt_list:
        
        # 이번 턴에 죽은 애들 구하기
        idxs = cnt_idxs[c]
        
        dead_set.update(idxs)
        
        # dead_set 길이가 k보다 작으면 절대 끝나지 않음
        # 놀랍게도 이거 안 넣으면 시간 초과 꽤 남
        if len(dead_set) < k:
            continue
        
        # 이번 턴에 죽은 돌의 위치부터 시작해서 연결이 끊긴 지점의 길이를 구함
        # 시작점부터 +, - 따로 뻗어나가면서 총 끊긴 길이 구하기
        for i in idxs:
            i_p = i + 1
            i_m = i - 1
            tmp_cnt = 1
            while i_p in dead_set:
                tmp_cnt += 1
                i_p += 1
            while i_m in dead_set:
                tmp_cnt += 1
                i_m -= 1
            
            # 만약 k보다 길 경우,
            # c번째로 징검다리를 건넌 사람까지만 통과하는 것이므로 c가 정답
            if tmp_cnt >= k:
                answer = c
                return answer