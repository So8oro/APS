import sys
sys.stdin = open('input.txt','r')

def f(k,N,r):
    global min_v,max_v
    if k==N:
        if min_v>r:
            min_v=r
        if max_v<r:
            max_v=r
    else:
        if PMMD[0] > 0:
            PMMD[0] -= 1
            f(k+1,N,r+nums[k])
            PMMD[0] += 1
        if PMMD[1] > 0:
            PMMD[1] -= 1
            f(k+1,N,r-nums[k])
            PMMD[1] += 1
        if PMMD[2] > 0:
            PMMD[2] -= 1
            f(k+1,N,r*nums[k])
            PMMD[2] += 1
        if PMMD[3] > 0:
            PMMD[3] -= 1
            if r // nums[k] < 0:
                d = -(abs(r) // abs(nums[k]))
            else:
                d = r // nums[k]
            f(k+1,N,d)
            PMMD[3] += 1


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    PMMD = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    min_v = 100000000000000000
    max_v = -100000000000000000

    # 함수에 전해줄 것은 몇번째숫자까지 했는가 / 몇번째숫자까지 해야하는가 / 현재 연산값
    f(1,N,nums[0])

    print(f'#{tc} {max_v-min_v}')



#1 24
#2 8
#3 144
#4 8
#5 91
#6 150
#7 198
#8 2160
#9 46652
#10 701696
