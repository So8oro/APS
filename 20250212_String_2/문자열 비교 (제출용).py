T = int(input())

for tc in range(1,T+1):
    result = 0
    str2 = input()
    str1 = input()
    N = len(str1)
    M = len(str2)
    i = j = 0

    while i<N and j<M:
        if str1[i] != str2[j]:
            i = i-j+1
            j=0
        else:
            i+=1
            j+=1
    if j==M:
        result = 1



    print(f'#{tc} {result}')