T = int(input())

for tc in range(1,T+1):

    A, B = input().split()
    A = list(A)

    len_A = init_len_A = len(A)
    len_B = len(B)
    i=j=count=0

    while True:
        while i<len_A and j<len_B:
            if A[i] != B[j]:
                i = i - j + 1
                j = 0
            else:
                i += 1
                j += 1
        if j == len_B:
            count += 1
            for _ in range(j):
                A.pop(i-j)
            i=j=0
            len_A = len(A)
        else:
            break

    print(f'#{tc} {init_len_A-(len_B-1)*count}')