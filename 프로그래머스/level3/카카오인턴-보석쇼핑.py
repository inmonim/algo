
# 최저 길이를 찾아, 0부터 n-max_length를 순회하며 시작점으로 잡고 찾기
def solution(gems):
    first_gem = {}
    for i in range(len(gems)):
        if gems[i] not in first_gem:
            first_gem[gems[i]] = i
    
    max_range = list(first_gem.values())[-1] + 1
    gem_type_count = len(first_gem)
    answer = [[]] * max_range
    
    for s in range(0, (len(gems)+1)-gem_type_count):
        tmp = set()
        
        for e in range(max_range):
            if s+e >= len(gems):
                break
            if gems[s + e] not in tmp:
                tmp.add(gems[s + e])
                if len(tmp) == gem_type_count:
                    max_range = e
                    answer[e] = [s+1, s+e+1]
    
    for x in answer:
        if x:
            answer = x
            break
    return answer

