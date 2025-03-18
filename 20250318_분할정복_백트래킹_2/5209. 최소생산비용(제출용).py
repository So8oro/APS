import sys
sys.stdin = open('input.txt','r')

def f(i, N, s):
    global min_v
    global cnt
    cnt += 1

    if i == N:
        if min_v > s:
            min_v = s
    elif min_v < s:
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    p = [i for i in range(N)]

    min_v = 1500
    cnt = 0

    f(0, N, 0)

    print(f'#{tc} {min_v}')