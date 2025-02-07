tc = int(input())

for tc in range(tc):
    list_len = int(input())
    num_list = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0

    i = 0

    while i < list_len:

        if num_list[i] >= num_list[max_idx]:
            max_idx = i
        if num_list[i] < num_list[min_idx]:
            min_idx = i

        i += 1

    print(f'#{tc+1} {abs(min_idx-max_idx)}')