import sys
sys.stdin = open('input.txt','r')

# 뒤에서부터 순회하자. 목적지에 도달할 수 있는 가장 빠른 정류장은 어디인가?
def f(E):
    global start
    global cnt
    if start == 1:
        return
    for i in range(E-1,0,-1):
        if M[i]+i >= E:
            start = i
    cnt += 1
    f(start)

T = int(input())

for tc in range(1,T+1):
    M = list(map(int,input().split()))
    N = M[0]

    start = 50
    cnt = 0

    f(N)

    print(f'#{tc} {cnt-1}')