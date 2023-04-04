def is_number(string): #check if input can be convert to float or not
    try:
        float(string)
        return True
    except ValueError:
        return False

def pop(stack):
    value = stack[-1]
    del stack[-1]
    return float(value)

stack = []
postfix_expr = input().split() #split input with empty spaces
#print(postfix_expr)

for token in postfix_expr:
    if is_number(token):
        stack.append(token) #append number into stack as string data type
    else: #If token is an operator
        first = pop(stack)
        second = pop(stack)
        switcher = {'+':second + first, '-':second - first, '*': second * first, '/':second / first, '%':second % first, '^':second ** first}
        stack.append(switcher.get(token))

print('%.1f' % stack[0])
