T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    stack = [0]*(N**2)
    top = -1
    path = 0
    arrived = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j]==2:                    # 출발점을 찾았습니다.
                while True:
                    arr[i][j]=5                     # 지나간 위치는 전부 5로 표시 하겠습니다.
                    for di,dj in direction:         # 네 방향을 살펴봅니다.
                        ni,nj = i+di,j+dj
                        if 0<=ni<N and 0<=nj<N:     # 인덱스 안에 있는 경우만 살펴봅니다.
                            if arr[ni][nj]==3:      # 도착했니?
                                arrived=1
                                break
                            if arr[ni][nj]==0:      # 길이 있다!
                                path += 1           # 길 하나 발견
                    if path==0:                     # 막다른 길입니다.
                        if top>=0:                   # 이전 갈림길이 있다면 그곳으로 돌아갑니다.
                            i,j = stack[top]
                            top -= 1
                        else:
                            break                   # 막다른 길인데 이전 갈림길도 없다? 탐색 종료.
                    elif path > 1:                  # 갈림길이네요.
                        top += 1
                        stack[top] = [i,j]          # 갈림길의 위치를 표시해둡니다.
                    if path>=1:                     # 길이 있었다면 길로 i,j를 업데이트 합시다. 귀찮으니 걍 다시 찾죠.
                        path = 0                    # path 초기화
                        for di, dj in direction:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < N and 0 <= nj < N:
                                if arr[ni][nj] == 0:
                                    i,j = ni,nj     # 업데이트! 이제 나가자
                                    break

    print(f'#{tc} {arrived}')