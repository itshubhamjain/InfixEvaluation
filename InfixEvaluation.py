def operator(c):
    if c is not "":
        return (c in "+-*/")
    else:
        return False


def priority(c):
    if c in "+-": return 0
    if c in "*/": return 1


def number(c):
    if c != "":
        return (c in "0123456789.")
    else:
        return False


def calc(op, num1, num2):
    if op == "+": return str(float(num1) + float(num2))
    if op == "-": return str(float(num1) - float(num2))
    if op == "*": return str(float(num1) * float(num2))
    if op == "/": return str(float(num1) / float(num2))


def Infix(expr):

    stackChr = list()
    stackNum = list()
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if len(expr) > 0:
            d = expr[0]
        else:
            d = ""
        if number(c):
            num += c
            if not number(d):
                stackNum.append(num)
                num = ""
        elif operator(c):
            while True:
                if len(stackChr) > 0:
                    top = stackChr[-1]
                else:
                    top = ""
                if operator(top):
                    if not priority(c) > priority(top):
                        if len(stackNum) is 0:
                            print("Invalid Expression")
                            exit(1)
                        num2 = stackNum.pop()
                        if len(stackChr) is 0:
                            print("Invalid Expression")
                            exit(1)
                        op = stackChr.pop()
                        if len(stackNum) is 0:
                            print("Invalid Expression")
                            exit(1)
                        num1 = stackNum.pop()
                        if len(expr) is not 0:
                            print("Invalid Expression")
                            exit(1)
                        stackNum.append(calc(op, num1, num2))
                    else:
                        stackChr.append(c)
                        break
                else:
                    stackChr.append(c)
                    break
        elif c == "(":
            stackChr.append(c)
        elif c == ")":
            while len(stackChr) > 0:
                if len(stackChr) is 0:
                    print("Invalid Expression")
                    exit(1)
                c = stackChr.pop()
                if c == "(":
                    break
                elif operator(c):
                    if len(stackNum) is 0:
                        print("Invalid Expression")
                        exit(1)
                    num2 = stackNum.pop()
                    if len(stackNum) is 0:
                        print("Invalid Expression")
                        exit(1)
                    num1 = stackNum.pop()
                    stackNum.append(calc(c, num1, num2))

    while len(stackChr) > 0:
        if len(stackChr) is 0:
            print("Invalid Expression")
            exit(1)
        c = stackChr.pop()
        if c == "(":
            if ')' not in stackChr:
                print("Invalid Expression")
                exit(1)
            break
        elif operator(c):
            if len(stackNum) is 0:
                print("Invalid Expression")
                exit(1)
            num2 = stackNum.pop()
            if len(stackNum) is 0:
                print("Invalid Expression")
                exit(1)
            num1 = stackNum.pop()
            stackNum.append(calc(c, num1, num2))
    if len(expr) is not 0:
        print("Invalid Expression")
    if len(stackNum) > 1 or len(stackNum)==0:
        print("Invalid Expression")
        exit(1)
    return stackNum.pop()


expr = input("Enter the string of expression you want to evaluate\n")
flag = 0
x=0
y=0
expr = list(expr)
err = ['1','2','3','4','5','6','7','8','9','0','(',')','/','*','+','-']
err1 = ['/','*','+','-']
err2 = ['(',')']
for item in expr:
    if item in err:
        flag=1
    else:
        flag=-1
        break

if flag is not 1:
    print("Invalid Expression")
    exit(1)

for item1 in expr:
    if item1 in err1:
        if x is 1:
            print("Invalid Expression")
            exit(1)
        else:
            x=1
    else:
        x=0
print(Infix(expr))