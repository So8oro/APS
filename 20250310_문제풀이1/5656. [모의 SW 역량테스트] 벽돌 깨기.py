import sys
sys.stdin = open('input.txt','r')

def f(N,W,current=[]):      # 중복 순열 생성
    if len(current)==N:
        shot.append(current)
        return

    for element in range(W):
        f(N,W,current+[element])




T = int(input())

for tc in range(1,T+1):
    N,W,H = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(H)]
    arr_copy = [row[:] for row in arr]

    #공을 떨어트리는 가능한 모든 경우의 수 모음
    shot = []
    f(N,W)

    #공을 떨어트립시다
    for one_try in shot:

        pop = 0

        for one_shot in one_try:
            for i in range(H):
                if arr[i]!=0:
                    stack = [[i,one_shot]]     # 처음 공이 떨어진 위치
                    break

            while stack:
                vi, vj = pop.stack






    print(f'#{tc}')