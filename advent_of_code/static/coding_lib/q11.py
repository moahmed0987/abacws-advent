def evaluate_expression(expression):
    operands = []
    operators = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            operand = int(expression[i])
            while i + 1 < len(expression) and expression[i+1].isdigit():
                operand = operand * 10 + int(expression[i+1])
                i += 1
            operands.append(operand)
        elif expression[i] in "+*":
            operators.append(expression[i])
        elif expression[i] == "(":
            j = i + 1
            count = 1
            while count > 0:
                if expression[j] == "(":
                    count += 1
                elif expression[j] == ")":
                    count -= 1
                j += 1
            operands.append(evaluate_expression(expression[i+1:j-1]))
            i = j - 1
        i += 1
    while operators:
        operator = operators.pop(0)
        if operator == "+":
            operands[1] += operands[0]
        elif operator == "*":
            operands[1] *= operands[0]
        operands.pop(0)
    return operands[0] 

def answer(expressions): 
    expressions = str(expressions)
    from ast import literal_eval
    expressions = literal_eval(expressions)

    return sum([evaluate_expression(expression.split()) for expression in expressions]) 

import random

def create_input():
    expression_list = []
    for _ in range(3):
        expression = ""
        for _ in range(random.randint(3, 5)):
            expression += str(random.randint(1, 9))
            expression += " "
            expression += random.choice(["+", "*"])
            expression += " "
            if random.random() < 0.3:
                expression += str(random.randint(1, 9))
                expression += " "
                expression += random.choice(["+", "*"])
                expression += " "                
            else:
                expression += "( "
                expression += generate_expression()
                expression += " )"
                expression += " "
                expression += random.choice(["+", "*"])
                expression += " "
            expression += str(random.randint(1, 9))
        expression_list.append(expression)
    return expression_list
            
def generate_expression():
    expression = ""
    expression += str(random.randint(1, 9))
    expression += " "
    expression += random.choice(["+", "*"])
    expression += " "
    expression += str(random.randint(1, 9))
    return expression