import sys, os

path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(path)

from module import stdin_time

@stdin_time
def sol(input):
    from collections import Counter
    input = sys.stdin.read()
    words, chars = input.split('-')[0].strip().split('\n'), input.split('-')[1].strip().split('\n')[:-1]

    char_list = []
    for char in chars:
        char_dict = Counter(char)
        wd = {i: 0 for i in char}
        char_list.append([char_dict, wd])
    for word in words:
        word_dict = Counter(word)
        for char_dict, wd in char_list:
            for k, v in word_dict.items():
                if k not in char_dict or char_dict[k] < v:
                    break
            else:
                for k in word_dict.keys():
                    wd[k] += 1

    for char_dict, wd in char_list:
        M, m = max(wd.values()), min(wd.values())
        Mk, mk = [], []
        for k, v in wd.items():
            if v == M:
                Mk.append(k)
            if v == m:
                mk.append(k)
        print(f"{''.join(sorted(mk))} {m} {''.join(sorted(Mk))} {M}")