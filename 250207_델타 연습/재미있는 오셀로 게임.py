T = int(input())

for tc in range(1,T+1):

    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(M)]

    board = [[0]*N for _ in range(N)]

    board[int(N/2)][int(N/2)], board[int(N/2)-1][int(N/2)-1] = 2, 2
    board[int(N/2)-1][int(N/2)], board[int(N/2)][int(N/2)-1] = 1, 1

    for i,j,color in arr:
        i -= 1
        j -= 1
        board[i][j] = color

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            for c in range(1, N):
                ni, nj = i + di * c, j + dj * c
                if 0 <= ni < N and 0 <= nj < M:
                    if board[ni][nj] == 0:
                        break
                    elif board[ni][nj] == color:
                        break
                    else:
                        pass

    print(board)





    print(f'#{tc}')