import sys

input = sys.stdin.readline

N = int(input())
answer = []

for _ in range(N):
    
    check_list = list(input())
    sum = 0
    
    for i in check_list:
        
        if i =='(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            break
    
    if sum == 0:
        answer.append('YES')
    else:
        answer.append('NO')

for i in range(0, len(answer)):
    print(answer[i])