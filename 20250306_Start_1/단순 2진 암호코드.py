import sys
sys.stdin = open('input.txt','r')

T = int(input())

keys = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
        }

for tc in range(1,T+1):

    N, M = map(int,input().split())
    odd_sum = 0
    even_sum = 0
    cnt = 0

    for _ in range(N):
        str = input()
        if str != '0'*M:
            code = str

    for i in range(M-1,0,-1):
        if code[i] == '1':
            end = i
            break

    for i in range(end-55,end,7):
        cnt += 1
        if cnt%2 == 1:
            odd_sum += keys[code[i:i+7]]
        else:
            even_sum += keys[code[i:i+7]]

    if (odd_sum*3+even_sum)%10==0:
        print(f'#{tc} {odd_sum+even_sum}')
    else:
        print(f'#{tc} 0')