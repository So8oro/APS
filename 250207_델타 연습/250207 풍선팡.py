T = int(input())

for tc in range(1,T+1):
    best_pang = 0
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            current_pang = arr[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for c in range(1,arr[i][j]+1):
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<M:
                        current_pang += arr[ni][nj]
            if best_pang < current_pang:
                best_pang = current_pang

    print(f'#{tc} {best_pang}')