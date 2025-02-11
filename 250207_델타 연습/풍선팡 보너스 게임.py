T = int(input())

for tc in range(1,T+1):
    max_pang = 0
    min_pang = 4000
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    delta = [[1,0],[0,1],[-1,0],[0,-1]]

    for i in range(N):
        for j in range(N):
            current_pang = arr[i][j]
            for n in range(1,N):
                for d in delta:
                    if i+n*d[0] in range(N) and j+n*d[1] in range(N):
                        current_pang += arr[i+n*d[0]][j+n*d[1]]

            if current_pang > max_pang:
                max_pang = current_pang
            if current_pang < min_pang:
                min_pang = current_pang





    print(f'#{tc} {max_pang - min_pang}')