T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [[0 for _ in range(N)] for _ in range(N)]  # 0으로 채워진 N x N 행렬
    loc = [0, 0]  # 초기 위치 설정
    num = 1  # 초깃값 설정
    # direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # for i in range(0, N):
    #     for j in range(0, N):
    for _ in range(N**2):
        arr[loc[0]][loc[1]] = num
        for di, dj in direction:
            ni = loc[0] + di
            nj = loc[1] + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:  # 유효한 범위에 있고, 아직 값이 채워지지 않은 경우
                loc = [ni, nj]
                if di == -1 and dj == 0:  # 다음 위치의 방향이 위쪽일 때 direction 탐색 순서 변경
                    direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                else:
                    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                break
        num += 1
    print(f'#{tc}')

    for n in range(N):
        print(*arr[n])