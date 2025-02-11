T = int(input())

for tc in range(1, T+1):

    N, M = map(int,input().split())
    palindrome = ''

    arr = [list(input()) for _ in range(N)]

    # 가로부터 확인
    for i in range(N):
        for j in range(N-M+1):      # 회문을 확인하는 구간의 첫 글자 인덱스
            for k in range(M//2):   # 회문의 길이 절반만큼 비교
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else:
                for k in range(M):
                    palindrome += arr[i][j+k]

    # 세로 확인
    for j in range(N):
        for i in range(N - M + 1):  # 회문을 확인하는 구간의 첫 글자 인덱스
            for k in range(M // 2):  # 회문의 길이 절반만큼 비교
                if arr[i+k][j] != arr[i+M-1-k][j]:
                    break
            else:
                for k in range(M):
                    palindrome += arr[i+k][j]


    print(f'#{tc} {palindrome}')