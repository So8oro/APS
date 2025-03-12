import sys
sys.stdin = open('input.txt','r')

T = int(input())


# 1부터 N까지 순열 생성
def f(N,p=[]):
    if len(p)==N-1:
        path.append([1]+p+[1])
        return
    for i in range(2,N+1):
        if i not in p:
            f(N,p+[i])

for tc in range(1,T+1):

    path = []
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_v = 1000

    f(N)

    for loop in path:
        v = 0
        for i in range(N):
            v += arr[loop[i]-1][loop[i+1]-1]
        if min_v > v:
            min_v = v

    print(f'#{tc} {min_v}')

