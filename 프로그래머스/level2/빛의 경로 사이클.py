from pprint import pprint

grid = ["SL","LR"]

def solution(grid):
    ol, il = len(grid)*2+1, len(grid[0])*2+1
    
    arr = [[0]*(il) for _ in range(ol)]
    
    for o in range(ol):
        for i in range(il):
            if not o%2:
                if i%2:
                    arr[o][i] = [1, 1]
            else:
                if i%2:
                    arr[o][i] = grid[o//2][i//2]
                else:
                    arr[o][i] = [1, 1]
    
    x, y, d = 1, 0, 0
    
    def start(x, y, d):
        cnt = 0
        while 1:
            pprint(arr)
            print("높이:", y, "좌우:", x, d)
            if not arr[y][x][d]:
                return cnt
            # 좌우
            if y%2:
                # 오른쪽으로 가고 있으면
                if d == 1:
                    arr[y][x][1] = 0
                    x += 1
                    x = x%il-1
                    # 위쪽으로 굴곡
                    if arr[y][x] == 'L':
                        y -= 1
                        if y < 0:
                            y = ol-2
                        d = 0
                    # 아래쪽으로 굴곡
                    elif arr[y][x] == 'R':
                        y += 1
                        y = y%ol-1
                        d = 1
                    # 직진
                    else:
                        x += 1
                        x = x%il-1
                # 왼쪽으로 가고 있으면
                else:
                    arr[y][x][0] = 0
                    x -= 1
                    if x < 0:
                        x = il-2
                    # 아래쪽으로 굴곡
                    if arr[y][x] == 'L':
                        y += 1
                        y = y%ol-1
                        d = 1
                    # 위쪽으로 굴곡
                    elif arr[y][x] == 'R':
                        y -= 1
                        if y < 0:
                            y = ol-2
                        d = 0
                    # 직진
                    else:
                        x -= 1
                        if x < 0:
                            x = il-2
            # 상하
            else:
                # 위로 올라가고 있으면
                if d == 0:
                    arr[y][x][0] = 0
                    y -= 1
                    if y < 0:
                        y = ol-2
                    # 왼쪽으로 굴곡
                    if arr[y][x] == 'L':
                        x -= 1
                        if x < 0:
                            x = il-2
                        d = 0
                    # 오른쪽으로 굴곡
                    elif arr[y][x] == 'R':
                        x += 1
                        x = x%il -1
                        d = 1
                    # 직진
                    else:
                        y -= 1
                        if y < 0:
                            y = y%ol -1
                    
                
                # 아래로 내려가고 있으면
                else:
                    arr[y][x][1] = 0
                    y += 1
                    y = (y%ol) - 1
                    # 오른쪽으로 굴곡
                    if arr[y][x] == 'L':
                        x += 1
                        x = x%il - 1
                        d = 1
                    elif arr[y][x] == 'R':
                        x -= 1
                        if x < 0:
                            x = il-2
                        d = 0
                    else:
                        y += 1
                        y = y%ol - 1
        
            cnt += 1
    c = 0
    x = start(x, y, d)
    
    return c

print(solution(grid))