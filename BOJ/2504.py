import sys

input = sys.stdin.readline

GH_input = list(input())
GH = []
score = 0
tmp = 1

for i in range(len(GH_input)):
    if GH_input[i] == '(':
        GH.append(GH_input[i])
        tmp *= 2
        
    elif GH_input[i] =='[':
        GH.append(GH_input[i])
        tmp *= 3
            
    elif GH_input[i] ==')':
        if not GH or GH[-1] == '[':
            score = 0
            break
        if GH_input[i-1] =='(':
            score += tmp   
        GH.pop()
        tmp //= 2
    
    else:
        if not GH or GH[-1] =='(':
            score = 0
            break
        if GH_input[i-1] == '[':
            score += tmp       
        GH.pop()
        tmp //= 3
        
if GH:
    print(0)
else:
    print(score)