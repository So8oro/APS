import sys
sys.stdin = open('input.txt','r')


def f(i):
    global ans
    if i==N:        # 퀸을 다 놓았구나!
        ans += 1
    else:
        for j in range(N):      # i,j 위치에 퀸을 놓아보자.
            place = True
            # 퀸을 놓을 수 있는지 확인해야함
            for di,dj in ((-1,-1),(-1,0),(-1,1)):   # 위쪽에 놓인 퀸 중에 범위 겹치는게 있나?
                if place is False:
                    break
                for k in range(1,N):
                    ni,nj = i+k*di,j+k*dj
                    if 0<=ni<N and 0<=nj<N:
                        if visited[ni][nj]==1:
                            place = False
                            break   # 겹치는 거 있음 안됨
                    else:
                        break
            if place:
                visited[i][j]=1     # 퀸 배치
                f(i+1)              # 다음 열 탐색
                visited[i][j]=0     # 퀸 배치 취소





T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ans = 0

    visited = [[0]*N for _ in range(N)]

    f(0)

    print(f'#{tc} {ans}')