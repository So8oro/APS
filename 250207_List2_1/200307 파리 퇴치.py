T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    NxN = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for ii in range(i,i+M):
                for jj in range(j,j+M):
                    kill += NxN[ii][jj]
            if max_kill < kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')