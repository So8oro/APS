T = int(input())

for tc in range(1, T+1):

    word = input()

    word_reversed = word[::-1]

    if word == word_reversed:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')