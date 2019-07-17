class Stack:
    def __init__(self):
        self.stackS = []

    def push(self, value):
        self.stackS.append(value)

    def printStack(self):
        print(self.stackS)

    def pops(self):
        self.stackS.pop()

    def isEmpty(self):
        return self.stackS == []

def parseChecker(parsingVal):
    balanced = True
    index = 0
    s = Stack()
    while index < len(parsingVal) and balanced:
        symbol = parsingVal[index]

        if symbol == '(':
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False

            else:
                s.pops()

        index += 1
        s.printStack()

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parseChecker("(())"))

