for tc in range(1, 11):

    N = int(input())

    stack = [0] * N
    top = -1

    infix = input()
    postfix = ''

    icp = {'+': 1, '*': 2}  # 연산자 우선순위
    for i in range(N):
        if '0' <= infix[i] <= '9':  # 피연산자인 경우
            postfix += infix[i]
        else:  # 연산자인 경우
            if top > -1 and icp[stack[top]] >= icp[infix[i]]:  # stack[top] 우선순위가 같거나 높으면  pop
                postfix += stack[top]
                top -= 1
            top += 1
            stack[top] = infix[i]
    while top > -1:  # 남아있는 연산자를 수식뒤에 붙임
        postfix += stack[top]
        top -= 1

    for i in postfix:
        try:
            if i not in ('+', '-', '*', '/', '.'):
                top += 1
                stack[top] = int(i)
            elif i == '+':
                stack[top - 1] = stack[top] + stack[top - 1]
                top -= 1
            elif i == '-':
                stack[top - 1] = stack[top - 1] - stack[top]
                top -= 1
            elif i == '*':
                stack[top - 1] = stack[top] * stack[top - 1]
                top -= 1
            elif i == '/':
                stack[top - 1] = stack[top - 1] // stack[top]
                top -= 1
        except:
            pass

    print(f'#{tc} {stack[0]}')