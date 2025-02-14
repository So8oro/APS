'''
def paper(n):
    if n>=2 and memo[n]==0:
        memo[n] = paper(n-1) + 2*paper(n-2)
    return memo[n]

T = int(input())

for tc in range(1,T+1):

    N = int(input())//10

    memo = [0]*(N+3)
    memo[1] = 1
    memo[2] = 3


    print(f'#{tc} {paper(N)}')
'''

def paper(n):
    f = [0]*(n+3)
    f[1] = 1
    f[2] = 3
    for i in range(3,n+1):
        f[i] = f[i-1]+2*f[i-2]
    return f[n]

T = int(input())

for tc in range(1,T+1):

    N = int(input())//10

    print(f'#{tc} {paper(N)}')