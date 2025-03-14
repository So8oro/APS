import sys
sys.stdin = open('input.txt','r')

T = int(input())

def f(i,j,num):
    if len(num)==7:
        settt.add(num)
        return
    else:
        for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni,nj = i+di,j+dj
            if 0<=ni<4 and 0<=nj<4:
                f(ni,nj,num+arr[ni][nj])


for tc in range(1,T+1):

    arr = [list(input().split()) for _ in range(4)]
    settt = set()

    for i in range(4):
        for j in range(4):

            f(i,j,arr[i][j])

    print(f'#{tc} {len(settt)}')