import sys
sys.stdin = open('input.txt','r')

T = int(input())

def f(i, B, sum):
    global result
    if i==N:
        if sum>=B and result > sum-B:
            result = sum-B
    else:
        f(i+1,B,sum+heights[i])
        f(i+1,B,sum)


for tc in range(1,T+1):

    N,B = map(int,input().split())
    heights = list(map(int,input().split()))

    # 그냥 죄다 더해버리는 함수를 만들자.
    result = 10000

    f(0,B,0)


    print(f'#{tc} {result}')

    # 1 1
    # 2 4
    # 3 27
    # 4 11
    # 5 42
    # 6 32
    # 7 2
    # 8 3
    # 9 25
    # 10 0
