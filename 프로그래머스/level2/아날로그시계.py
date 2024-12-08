def solution(h1, m1, s1, h2, m2, s2):
    
    start_at = sum([h1*3600, m1*60, s1])
    end_at = sum([h2*3600, m2*60, s2])
    
    h1 = ((h1 * 3600) + (m1*60) + (s1)) % 43200
    m1 = (m1 * 720) + (s1*60)
    s1 = s1 * 720
    
    cnt = 0
    
    over_h = 0 if s1 <= h1 else 1
    over_m = 0 if m1 <= h1 else 1
    
    while start_at < end_at:
        print(h1, m1, s1, cnt)
        if h1 == m1 and m1 == s1:
            cnt += 1
            over_h, over_m = 1, 1
            h1 += 1
            m1 += 60
            s1 += 720
            continue
        
        h1 += 1
        m1 += 60
        s1 += 720
        
        if not over_h and s1 >= h1:
            cnt += 1
            over_h = 1
        if not over_m and s1 >= m1:
            cnt += 1
            over_m = 1
        
        if s1 >= 43200:
            s1 = 0
            over_h, over_m = 0, 0
        
        if m1 >= 43200:
            m1 = 0
        
        if h1 >= 43200:
            h1 = 0
        
        start_at += 1
            
    return cnt

print(solution(0, 0, 0, 23, 59, 59))