import sys
sys.stdin = open('input.txt','r')

T = int(input())

keys = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
        }

hex_dict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5': '0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

for tc in range(1,T+1):

    N,M = map(int,input().split())

    # N개의 줄을 읽어오자
    arr = [input() for _ in range(N)]

    '''
    이하 코드는 0을 기준으로 16진수만 빼오려 하였으나 16진수 중간에도 0이 들어가있는 경우가 있어서 폐기 처분됨
    
    # 읽어온 줄에서 0이 아닌 것을 찾으면, 전체 내용을 저장하자
    for i in range(N):
        for j in range(M):
            code = ''
            if arr[i][j] != '0':    # 코드 시작점 발견
                for k in range(M):
                    if arr[i][j+k] != '0':
                        code += arr[i][j+k]
                        arr[i][j+k] = '0'
                        for k2 in range(1,N):
                            if arr[i+k2][j+k] != '0':
                                arr[i+k2][j+k] = '0'
                            else:
                                break
                    else:
                        break
                print(code)
    # 그리고 해당 코드를 전부 삭제해야함
    # 아래로 내려가면서 삭제
    '''
    result = 0

    # 전부 이진코드로 변환한 4배 리스트를 만들자
    bin_arr = []
    for i in range(N):
        line = ''
        for j in range(M):
            line += hex_dict[arr[i][j]]
        bin_arr.append(line)

    # 왼쪽에서부터 탐색하여서 1을 찾자
    mult = 0
    for i in range(N):
        for j in range(M*4-1,-1,-1):
            if bin_arr[i][j]=='1':
            # 몇 배율짜리인가? 전체 길이는 얼마나 되는가?
                c1, c2, c3 = 0,0,0      # 첫번째 1 길이, 첫번째 0 길이, 두번째 1 길이
                for k in range(M*4):
                    if bin_arr[i][j-k]=='1' and c2==0:
                        c1 += 1
                    elif bin_arr[i][j-k]=='0' and c3==0:
                        c2 += 1
                    elif bin_arr[i][j-k]=='1':
                        c3 += 1
                    else:
                        break
                mult = min(c1,c2,c3)

                # 찾은 코드 저장 + 해당 길이만큼 + 아래로 이어진 만큼 0으로 비워주자
                code = bin_arr[i][j-mult*56+1:j+1]

                end_code = 0

                for k in range(N):
                    if bin_arr[i+k][j]=='0':
                        end_code = i+k
                        break
                for k in range(i,end_code):
                    bin_arr[k] = bin_arr[k][0:j-mult*56+1] + '0'*mult*56 + bin_arr[k][j+1:]


                # 찾은 코드를 숫자 리스트로 변환
                real_code = []
                temp = ''
                cnt = 0
                for idx in range(0,56*mult,mult):
                    cnt += 1
                    temp += code[idx]
                    if cnt == 7:
                        real_code.append(keys[temp])
                        temp = ''
                        cnt = 0

                # 찾은 코드 유효성 검사 및 합계 저장
                if ((real_code[0]+real_code[2]+real_code[4]+real_code[6])*3+real_code[1]+real_code[3]+real_code[5]+real_code[7])%10==0:
                    result += sum(real_code)

    # 코드 찾기 반복




    print(f'#{tc} {result}')