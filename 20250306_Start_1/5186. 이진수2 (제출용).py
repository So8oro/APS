# import sys
# sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1,T+1):

    N = float(input())
    result = ''

    for pow in range(-1,-15,-1):
        if N==0:
            break
        if N>=2**pow:
            result += '1'
            N -= 2**pow
        else:
            result += '0'
    else:
        result = 'overflow'


    print(f'#{tc} {result}')