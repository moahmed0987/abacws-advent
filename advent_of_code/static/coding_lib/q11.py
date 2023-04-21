Operators = set(['+', '-', '*', '/', '(', ')'])  # collection of Operators
Priority = {'+':1, '-':1, '*':2, '/':2} # dictionary having priorities of Operators

def infixToPostfix(expression): 
    stack = [] # initialization of empty stack
    output = ''   
    for character in expression:
        if character.isdigit():  # if an operand append in postfix expression
            output+= character
        elif character=='(':  # else Operators push onto stack
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        elif character in Operators:
            while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    return output

def do_math(operator, operand1, operand2):
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
        case "/":
            return operand1 / operand2

def answer(expressions):
    answers = []
    for expression in expressions:
        operand_stack = []
        for character in expression:
            if character.isdigit():
                operand_stack.append(int(character))
            elif character in Operators:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(character, operand1, operand2)
                operand_stack.append(result)
        answers.append(operand_stack.pop())
    return sum(answers)

import random

def create_input():
    expression_list = []
    for _ in range(3):
        expression = ""
        for _ in range(random.randint(3, 5)):
            expression += str(random.randint(1, 9))
            expression += " "
            expression += random.choice(["+", "*", "-", "/"])
            expression += " "
            if random.random() < 0.3:
                expression += str(random.randint(1, 9))
                expression += " "
                expression += random.choice(["+", "*", "-", "/"])
                expression += " "                
            else:
                expression += "( "
                expression += generate_expression()
                expression += " )"
                expression += " "
                expression += random.choice(["+", "*", "-", "/"])
                expression += " "
            expression += str(random.randint(1, 9))
        expression_list.append(expression)
    return expression_list
            
def generate_expression():
    expression = ""
    expression += str(random.randint(1, 9))
    expression += " "
    expression += random.choice(["+", "*", "-", "/"])
    expression += " "
    expression += str(random.randint(1, 9))
    return expression