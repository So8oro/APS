import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr.sort(key=lambda x:(x[1]))

    end_time = arr[0][1]
    cnt = 1

    for start,end in arr:
        if end_time <= start:
            cnt += 1
            end_time = end


    print(f'#{tc} {cnt}')