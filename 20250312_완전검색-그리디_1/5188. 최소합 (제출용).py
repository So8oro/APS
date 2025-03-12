import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dp = [[0]*N for _ in range(N)]
    dp[0][0] = arr[0][0]

    for i in range(N):
        for j in range(N):
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]
            elif i > 0:
                dp[i][j] = dp[i - 1][j] + arr[i][j]
            elif j > 0:
                dp[i][j] = dp[i][j - 1] + arr[i][j]


    print(f'#{tc} {dp[N-1][N-1]}')