def infix_to_postfix(exprassion):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    tokens = exprassion.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())

    return ' '.join(output)
expr1 = "5 + ( 6 - 2 ) * 9"
expr2 = "( 1 + 2 ) * ( 3 + 4 )"

print( infix_to_postfix(expr1))
print( infix_to_postfix(expr2))
