'''
### 재귀함수를 사용하는 방법

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

for tc in range(1,11):

    N, arr = input().split()
    arr = list(arr)

    pw = ''.join(remove_char_in_row(arr))


    print(f'#{tc} {pw}')

이하는 스택을 사용하는 방법으로 재작성
'''

for tc in range(1,11):
    N, str1 = input().split()
    N = int(N)
    stack = [None]*N
    top = -1

    for i in str1:
        if top == -1 or stack[top] != i:
            top += 1
            stack[top] = i
        else:
            top -= 1

    print(f'#{tc} ', end='')
    for i in range(top+1):
        print(stack[i], end='')
    print()