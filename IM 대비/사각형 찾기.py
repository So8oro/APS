T = int(input())

for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_area = 0

    for i in range(N):
        for j in range(N):
            length, height = 1, 1
            if arr[i][j] == 1:
                for k in range(1,N):
                    ni, nj = i, j+k
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] == 1:
                            length += 1
                        else:
                            break
                for k in range(1,N):
                    ni, nj = i+k, j
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] == 1:
                            height += 1
                        else:
                            break
                if max_area < height*length:
                    max_area = height*length

    print(f'#{1} {max_area}')