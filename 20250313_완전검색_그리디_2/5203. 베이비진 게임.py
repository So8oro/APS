import sys
sys.stdin = open('input.txt','r')

T = int(input())

def isbabygin(p):
    cnt = 0
    for i in p:
        if i:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3 or i == 3:
            return 1
    return

for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    p1 = [0]*10
    p2 = [0]*10
    result = 0
    for i in range(0,12,2):

        if result:
            break

        p1[arr[i]] += 1
        if isbabygin(p1):
            result = 1
            break

        p2[arr[i+1]] += 1
        if isbabygin(p2):
            result = 2
            break

    print(f'#{tc} {result}')