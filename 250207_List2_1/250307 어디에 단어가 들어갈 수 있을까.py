T = int(input())

for tc in range(1, T+1):
    result = 0
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 가로 먼저 체크합시다
    # 1이 연속으로 K개 등장하고, 그 양 끝은 0이거나 리스트의 끝이어야 합니다
    for i in range(N):
        for j in range(N-K+1):
            if all(puzzle[i][j+a]==1 for a in range(K)):
                # 양 끝이 0이거나 리스트의 끝인지 체크. index out 을 막기 위해 각각 체크합니다.
                if j==0 and j+K==N:
                    result += 1
                elif j==0 and puzzle[i][j+K]==0:
                    result += 1
                elif puzzle[i][j-1]==0 and j+K==N:
                    result += 1
                elif puzzle[i][j-1]==0 and puzzle[i][j+K]==0:
                    result += 1
    # 세로도 합시다
    for j in range(N):
        for i in range(N-K+1):
            if all(puzzle[i+a][j]==1 for a in range(K)):
                if i==0 and i+K==N:
                    result += 1
                elif i==0 and puzzle[i+K][j]==0:
                    result += 1
                elif puzzle[i-1][j]==0 and i+K==N:
                    result += 1
                elif puzzle[i-1][j]==0 and puzzle[i+K][j]==0:
                    result += 1

    print(f'#{tc} {result}')


