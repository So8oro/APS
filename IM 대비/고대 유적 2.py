T = int(input())

for tc in range(1,T+1):

    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_count = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j]==1:
                for di,dj in [[0,1],[1,0]]:
                    count = 0
                    for n in range(max(N,M)):
                        ni = i+n*di
                        nj = j+n*dj
                        if 0<=ni<N and 0<=nj<M:
                            if arr[ni][nj]==1:
                                count += 1
                                if max_count<count:
                                    max_count=count
                            else:
                                count = 0
                                break

    if max_count==1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {max_count}')
