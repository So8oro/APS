T = int(input())

def remove_char_in_row(arr):
    poped = None
    for i in range(1,len(arr)):
        if 1<=i<len(arr):
            if arr[i]==arr[i-1]:
                poped = arr.pop(i-1)
                arr.pop(i-1)

    if poped is None:
        return

    remove_char_in_row(arr)

    return arr

for tc in range(1,T+1):

    arr = remove_char_in_row(list(input()))


    print(f'#{tc} {len(arr)}')