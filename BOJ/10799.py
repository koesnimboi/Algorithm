import sys

input = sys.stdin.readline

inputs = list(input())
sum = 0
st = []

for i in range(len(inputs)):
    if inputs[i] == '(':
        st.append('(')
    
    else:
        if inputs[i-1] =='(':
            st.pop()
            sum += len(st)
        else:
            st.pop()
            sum += 1
    
print(sum)