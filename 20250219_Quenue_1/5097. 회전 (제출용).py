T = int(input())

for tc in range(1,T+1):

    N,M = map(int,input().split())

    arr = list(input().split())

    print(f'#{tc} {arr[M%N]}')