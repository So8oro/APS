T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    arr3 = []
    count = 0
    count2 = 0

    for i in range(N+M):

        if i%2==0:
            try:
                arr3.append(arr.pop(0))
            except:
                arr3.append(arr2.pop(0))

        else:
            try:
                arr3.append(arr2.pop(0))
            except:
                arr3.append(arr.pop(0))

        count += 1

    print(f'#{tc}',*arr3)


