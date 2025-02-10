T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    i,j,num = 0,-1,0

    while num < N**2:                               # N**2 번 칸을 채워야 한다.
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  
            i += di                                 # 다음칸을 살펴보자. 이를 위해 i,j 를 0,-1로 시작했다.
            j += dj
            while 0<=i<N and 0<=j<N:                # 인덱스 안에 있는 동안 계속 반복한다.
                if arr[i][j]==0:                    # 살펴보는 칸이 비어있는 경우에만
                    num += 1                        # 해당칸에 다음숫자를 삽입한다.
                    arr[i][j] = num
                    i += di                         # 그리고 다음칸으로 다시 넘어간다.
                    j += dj
                else:                               # 이미 값이 있는 칸을 만났다면, 다음 for문으로 넘어가서 다음 델타를 적용한다.
                    break
            i -= di                                 # 현재 돌아야 하는 범위를 벗어났다면, 다시 집어넣어주자.
            j -= dj


    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()