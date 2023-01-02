from typing import List


def evalRPN(tokens: List[str]) -> int:
    exp = []
    for token in tokens:
        if token == "*":
            exp.append(exp.pop()*exp.pop())
        elif token == "+":
            exp.append(exp.pop()+exp.pop())
        elif token == "-":
            x, y = exp.pop(),exp.pop()
            exp.append(y-x)
        elif token == "/":
            x,y = exp.pop(), exp.pop()
            exp.append(int(y/x))
        else:
            exp.append(int(token))


    return exp[0]
    

print(evalRPN(["2", "1", "+", "3", "*"]))
