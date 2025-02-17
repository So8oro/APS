T = int(input())

for tc in range(1,T+1):

    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    flips = [list(map(int,input().split())) for _ in range(M)]

    for flip in flips:

        for d in range(1,flip[1]+1):
            if 0<=flip[0]-1-d<N and 0<=flip[0]-1+d<N:
                if arr[flip[0]-1-d] == arr[flip[0]-1+d]:
                    if arr[flip[0]-1-d]==0:
                        arr[flip[0] - 1 - d],arr[flip[0]-1+d]=1,1
                    else:
                        arr[flip[0] - 1 - d], arr[flip[0] - 1 + d] = 0,0


    print(f'#{tc}',*arr)