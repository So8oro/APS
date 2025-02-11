T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'

    # 위쪽, 좌측부터 돌을 탐색하고, 해당 돌부터 시작하는 오목이 있는지 체크하자.
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='o':
                # 오른쪽, 아래쪽, 양쪽 대각선의 5곳을 순서대로 체크하자.
                for di, dj in [[0,1],[1,0],[1,1],[1,-1]]:
                    for c in range(1,5):
                        ni, nj = i+c*di, j+c*dj
                        if 0<=ni<N and 0<=nj<N:
                            if arr[ni][nj] == '.':
                                break       # 오목이 아니므로 탈출
                        else:
                            break           # 인덱스에서 벗어나도 오목이 될 수 없는 것
                    else:
                        result = 'YES'  # 오목 찾음
                        break

    print(f'#{tc} {result}')