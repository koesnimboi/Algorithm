from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
d = deque([])
answer = []

for i in range(N):
    x = input()
    z = x.split()

    if z[0] == 'push':
        d.append(z[1])
        
    elif z[0] == 'pop':
        if len(d) ==0:
            answer.append(-1)
        else:
            answer.append(d.popleft())
    
    elif z[0] =='size':
        answer.append(len(d))
        
    elif z[0] == 'empty':
        if len(d) == 0:
            answer.append(1)
            
        else:
            answer.append(0)
            
    elif z[0] == 'front':
        if len(d) == 0:
            answer.append(-1)
        
        else:
            answer.append(d[0])
    
    elif z[0] == 'back':
        if len(d) == 0:
            answer.append(-1)
        
        else:
            answer.append(d[-1])
                
for i in range(len(answer)):
    print(answer[i])