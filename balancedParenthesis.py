x = input("Plz Enter the string of parenthesis :")
stack = []
mapping = {'(':')','[':']','{':'}'}
for c in x:
    if c in '([{':
        stack.append(c)
    elif c in ')]}':
        if not stack and stack[-1] != mapping(c):
            print("Not in Balanced Mode")
            break
        else:
            stack.pop()
if not stack:
    print("Balanced")
else:
    print("Not Balanced")
            

        