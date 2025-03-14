import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):

    d,m,q,y = map(int,input().split())
    plan = list(map(int,input().split()))

    min_c = [0]*12

    min_c[0] = min(d*plan[0],m)
    min_c[1] = min(d*plan[1],m) + min_c[0]
    min_c[2] = min((min(d*plan[2],m) + min_c[1]),q)

    for i in range(3,12):
        min_c[i] = min(min_c[i-3]+q,min_c[i-1]+m,min_c[i-1]+d*plan[i])

    print(f'#{tc} {min(min_c[11],y)}')