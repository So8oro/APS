T = int(input())

for tc in range(1,T+1):
    case = input()
    result = 1
    arr = []

    for i in case:
        try:
            if i == '{' or i == '(':
                arr.append(i)
            elif i == ')':
                poped = arr.pop()
                if poped != '(':
                    result = 0
                    break
            elif i == '}':
                poped = arr.pop()
                if poped != '{':
                    result = 0
                    break
        except:
            result = 0
            break

    if arr != []:
        result = 0

    print(f'#{tc} {result}')