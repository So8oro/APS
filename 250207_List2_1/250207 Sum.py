for _ in range(10):
    case = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    max_sum = 0
    for j in range(100):
        max_sum += arr[0][j]    # max_sum 초기값 세팅

    # 각 행의 합
    for i in range(100):
        loc_sum = 0
        for j in range(100):
            loc_sum += arr[i][j]
        if loc_sum > max_sum:
            max_sum = loc_sum

    # 각 열의 합
    for j in range(100):
        loc_sum = 0
        for i in range(100):
            loc_sum += arr[i][j]
        if loc_sum > max_sum:
            max_sum = loc_sum

    # 대각선 합 우하향
    loc_sum = 0
    for i in range(100):
        for j in range(100):
            if i==j:
                loc_sum += arr[i][j]
        if loc_sum > max_sum:
            max_sum = loc_sum

    # 대각선 합 우상향
    loc_sum = 0
    for i in range(100):
        for j in range(100):
            if i+j==99:
                loc_sum += arr[i][j]
        if loc_sum > max_sum:
            max_sum = loc_sum

    print(f'#{case} {max_sum}')