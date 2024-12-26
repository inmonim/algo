def infinite_loop_example():
    # 배열과 탐색 범위 설정
    arr = [1, 2, 3, 4, 5, 6, 7, 8]  # 단순한 배열
    target = 8

    # 탐색 범위 초기화
    start, end = 0, len(arr) - 1

    # 잘못된 이진 탐색 코드 (mid 값을 포함하여 계속 탐색)
    for _ in range(10):
        mid = (start + end) // 2
        print(f"start: {start}, mid: {mid}, end: {end}, arr[mid]: {arr[mid]}")

        if arr[mid] == target:
            return
        elif arr[mid] < target:
            start = mid
        else:
            end = mid

# 실행
infinite_loop_example()