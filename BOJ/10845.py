import sys

input = sys.stdin.readline

N = int(input())
que = []
answers = []

for _ in range(N):
    inputs = input().split(' ')
    
    if inputs[0] == 'push':
        que.append(inputs[1])
    
    elif inputs[0] == 'pop':
        if len(que) != 0 :
            answers.append(que[0])
            que.pop(0)
            
        else:
            answers.append(-1)
            
    elif inputs[0] == 'size':
        answers.append(len(que))
    
    elif inputs[0] == 'empty':
        if len(que) == 0:
            answers.append(1)
        else:
            answers.append(0)
    
    elif inputs[0] == 'front':
        if len(que) != 0:
            answers.append(que[0])
        
        else:
            answers.append(-1)
            
    else:
        if len(que) != 0:
            answers.append(que[-1])
        else:
            answers.append(-1)

for i in range(len(answers)):
    print(answers[i])