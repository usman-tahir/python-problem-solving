
import stack

# A simple parentheses checker
def parentheses_checker(symbol_string):
    s = stack.Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.empty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.empty():
        return True
    else:
        return False

# A more generalized bracket checker
def bracket_checker(symbol_string):
    s = stack.Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.empty():
        return True
    else:
        return False

def matches(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)
