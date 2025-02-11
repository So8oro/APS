T = int(input())

for tc in range (1, T+1):

    str1 = list(input())
    str2 = list(input())
    str_dict = {}

    for str in str1:
        str_dict[str] = 0

    for str in str2:
        if str in str_dict:
            str_dict[str] += 1

    print(f'#{tc} {max(str_dict.values())}')