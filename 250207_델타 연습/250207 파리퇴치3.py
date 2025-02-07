T = int(input())

for tc in range(1,T+1):
    best_kill = 0
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 십자 형태로 스프레이를 뿌려보자
    for i in range(N):
        for j in range(N):
            current_kill = arr[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for c in range(1,M):                        # 중심도 스프레이 범위에 포함되네요..?
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        current_kill += arr[ni][nj]
            if best_kill < current_kill:
                best_kill = current_kill

    # 엑스자 형태로 스프레이를 뿌려보자
    for i in range(N):
        for j in range(N):
            current_kill = arr[i][j]
            for di, dj in [[1,1],[1,-1],[-1,1],[-1,-1]]:       # 여기만 수정하면 끝
                for c in range(1,M):
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        current_kill += arr[ni][nj]
            if best_kill < current_kill:
                best_kill = current_kill

    print(f'#{tc} {best_kill}')