import sys
sys.stdin = open('input.txt','r')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    time = 1
    arr = [0]*201

    for _ in range(N):
        start, end = map(int, input().split())

        if start > end:  # 시작점 숫자가 더 작도록 조정
            start, end = end, start

        for idx in range((start+1)//2,(end+1)//2+1):
            arr[idx] += 1

    print(f'#{tc} {max(arr)}')