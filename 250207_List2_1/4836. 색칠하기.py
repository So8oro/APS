T=int(input())
for t in range(1, T+1):
    N=int(input())
    o=[[0]*10 for _ in range(10)]
    p=0
    for _ in range(N):
        a,b,c,d,e=map(int,input().split())
        for i in range(a,c+1):
            for j in range(b,d+1):
                if o[i][j]==0:
                    o[i][j]=e
                else:
                    p+=1
    print(f'#{t} {p}')