T = int(input())

for tc in range(1,T+1):

    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    flips = [list(map(int,input().split())) for _ in range(M)]

    for flip in flips:
        color = arr[flip[0]-1]
        for i in range(flip[0]-1, flip[0]-1+flip[1]):
            if i<N:
                arr[i] = color

    print(f'#{tc}',*arr)