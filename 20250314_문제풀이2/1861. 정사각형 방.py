import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 각 번호에 인접한 이동 경로가 있는지를 체크하자.
    path = [0]*(N**2+1)

    for i in range(N):
        for j in range(N):
            for di,dj in ((0,1),(1,0),(-1,0),(0,-1)):
                ni,nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == arr[i][j] + 1:
                        path[arr[i][j]] = 1

    cnt = 0
    maxcnt = 0


    for i in range(N**2+1):
        if path[i] == 1:
            cnt += 1
        else:
            if maxcnt < cnt:
                idx = i-cnt
                maxcnt = cnt
            cnt = 0



    print(f'#{tc} {idx} {maxcnt+1}')

    # 1 6 8
    # 2 3 2
    # 3 149 2
    # 4 2 45
    # 5 2 23
    # 6 1 2
    # 7 1 4
    # 8 5 17
    # 9 4 2
    # 10 1 35
    # 11 2 2
    # 12 7 2
    # 13 45 2
    # 14 113 2
    # 15 12 32
    # 16 6 9
    # 17 1 4
    # 18 36 42
    # 19 204 2
    # 20 7 14
    # 21 4 2
    # 22 8225 2200
    # 23 35 3
    # 24 2 2
    # 25 613 2
    # 26 33 2
    # 27 5 5
