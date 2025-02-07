T = int(input())

for tc in range(1, T+1):
    result = 0
    N, K = map(int, input().split())

    n = 12
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]


    for i in range(1<<n):
        setsum = 0
        setcount = 0
        for j in range(n):
            if i&(1<<j):
                setsum += arr[j]
                setcount += 1
        if setsum == K and setcount == N:
            result += 1

    print(f'#{tc} {result}')