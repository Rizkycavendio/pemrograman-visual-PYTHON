# Muhammad Rizky Cavendio - 20051397011

Operators = set(['+', '-', '*', '/', '(', ')', '^'])
Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

def infixToPostfix(expression):
    stack = []
    output = ''

    for character in expression:

        if character not in Operators:

            output += character

        elif character == '(':

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()

            stack.append(character)

    while stack:
        output += stack.pop()

    return output


expression = "5*(4-2)"

print('infix: ', expression)

print('postfix: ', infixToPostfix(expression))

print('hasil:')