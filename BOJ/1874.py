import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []
count = 1
X = True

for _ in range(N):
    num = int(input())
    
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
        
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        X = False
        break

if X == True:
    for i in result:
        print(i)