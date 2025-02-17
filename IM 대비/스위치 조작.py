T = int(input())

for tc in range(1,T+1):

    N = int(input())
    arr = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    count = 0

    for i in range(N):
        if (count%2==0 and arr[i] != arr2[i]) or (count%2==1 and arr[i]==arr2[i]):
            count += 1

    print(f'#{tc} {count}')