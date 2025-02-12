for tc in range(1,11):

    N = int(input())
    arr = [list(input()) for _ in range(8)]
    count = 0

    # 가로부터 확인
    for i in range(8):
        for j in range(8 - N + 1):  # 회문을 확인하는 구간의 첫 글자 인덱스
            for k in range(N // 2):  # 회문의 길이 절반만큼 비교
                if arr[i][j + k] != arr[i][j + N - 1 - k]:
                    break
            else:
                count += 1

    # 세로 확인
    for j in range(8):
        for i in range(8 - N + 1):  # 회문을 확인하는 구간의 첫 글자 인덱스
            for k in range(N // 2):  # 회문의 길이 절반만큼 비교
                if arr[i + k][j] != arr[i + N - 1 - k][j]:
                    break
            else:
                count += 1

    print(f'#{tc} {count}')