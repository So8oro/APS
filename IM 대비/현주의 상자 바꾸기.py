T = int(input())

for tc in range(1,T+1):

    N,Q = map(int,input().split())
    arr = [0]*N

    for i in range(1,Q+1):
        L,R = map(int,input().split())
        for k in range(L-1,R):
            arr[k]=i

    print(f'#{tc}', *arr)