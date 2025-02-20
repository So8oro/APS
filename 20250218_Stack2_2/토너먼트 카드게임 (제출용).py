T = int(input())

def winner(i,j):        # 인덱스 두 개를 집어 넣었을 때 승자의 인덱스를 반환
    if arr[i]+1==arr[j] or arr[i]-2==arr[j]:
        return j
    else:
        return i

def f(i,j):     # 리스트의 시작과 끝 인덱스
    if i==j:
        return i
    # elif i+1==j:
    #     return winner(i,j)
    else:
        return winner(f(i,(i+j)//2),f((i+j)//2+1,j))

for tc in range(1,T+1):

    N = int(input())
    arr = list(map(int,input().split()))

    print(f'#{tc} {f(0,N-1)+1}')