import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    from collections import Counter
    words = set()
    chars = []
    while (i := input().strip()) != "-":
        words.add(i)
    while (i := input().strip()) != "#":
        chars.append(i)

    # 문자판으로 순회
    for char in chars:
        # 문자판에 쓰인 문자 카운트
        char_cnt = Counter(char)
        # 결과에 쓰일 문자 카운트
        wd = {i: 0 for i in char}
        # 문제 단어로 순회
        for word in words:
            # 문제 단어에 쓰인 문자 카운트
            # 이 부분이 사용 시간을 늘림. 문자판마다 문제를 순회하므로, words마다 새롭게 word_cnt를 계속 생성하므로 시간이 길어지는듯
            word_cnt = Counter(word)
            for k, v in word_cnt.items():
                # 문자판에 없거나, 문자판보다 많은 문자가 쓰인 경우 탈출
                if k not in char_cnt or char_cnt[k] < v:
                    break
            # 쓰일 수 있는 단어라면
            else:
                # 결과 카운트에 문자 카운트 + 1,
                # + v 할 경우, 중복 문자마다 카운트가 높아지므로 결과 도출이 안 됨
                for k in word_cnt.keys():
                    wd[k] += 1
        
        # 가장 많이 쓰인 단어들의 카운트, 적게 쓰인 단어들의 카운트
        M, m = max(wd.values()), min(wd.values())
        Mk, mk = [], []
        for k, v in wd.items():
            # 해당 문자가 가장 많이 쓰인 단어면 Mk에 저장
            if v == M:
                Mk.append(k)
            # 적게 쓰인 단어면 mk 저장
            if v == m:
                mk.append(k)
                
        # 오름차순 정렬 후 결과 출력
        print(f"{''.join(sorted(mk))} {m} {''.join(sorted(Mk))} {M}")