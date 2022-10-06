import sys
input = sys.stdin.readline

N = int(input())
form = input()
nums = [0] * N

for i in range(N):
    nums[i] = int(input())
    
stack = []

for i in form:
    if 'A' <= i <= 'Z':
        stack.append(nums[ord(i)-ord('A')])
        
    else:
        str2 = stack.pop()
        str1 = stack.pop()
        
        if i == '+':
            stack.append(str1+str2)
        elif i == '-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1*str2)
        elif i == '/':
            stack.append(str1/str2)
            
print('%.2f'%stack[0])