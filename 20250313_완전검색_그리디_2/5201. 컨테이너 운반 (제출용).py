import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):

    N,M = map(int,input().split())
    Wi = list(map(int,input().split()))
    Ti = list(map(int,input().split()))

    Wi.sort(reverse=1)
    Ti.sort(reverse=1)

    weight_sum = 0

    for truck in Ti:
        while Wi:
            if truck >= Wi[0]:
                weight_sum += Wi[0]
                Wi.pop(0)
                break
            else:
                Wi.pop(0)

    print(f'#{tc} {weight_sum}')