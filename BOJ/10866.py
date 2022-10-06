from collections import deque
import sys

N = int(input())
D = deque([])
answer = []

for _ in range(N):
    x = input()
    z = x.split(' ')
    
    if z[0] == 'push_front':
        D.appendleft(z[1])
        
    elif z[0] == 'push_back':
        D.append(z[1])
        
    elif z[0] == 'pop_front':
        if len(D) > 0:
            answer.append(D.popleft())
        else:
            answer.append(-1)
            
    elif z[0] == 'pop_back':
        if len(D) > 0:
            answer.append(D.pop())
        else:
            answer.append(-1)
        
    elif z[0] == 'size':
        answer.append(len(D))
        
    elif z[0] == 'empty':
        if len(D) == 0:
            answer.append(1)
        else:
            answer.append(0)
    
    elif z[0] == 'front':
        if len(D) > 0:
            answer.append(D[0])
        else:
            answer.append(-1)
            
    elif z[0] == 'back':
        if len(D) > 0:
            answer.append(D[-1])
        else:
            answer.append(-1)

for i in range(len(answer)):
    print(answer[i])