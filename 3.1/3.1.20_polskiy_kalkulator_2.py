def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


def invoke_operation(operator: str, state: list):
    if operator == '*':
        num2 = int(state.pop())
        num1 = int(state.pop())
        state.append(num1 * num2)
    elif operator == '/':
        num2 = int(state.pop())
        num1 = int(state.pop())
        state.append(num1 // num2)
    elif operator == '+':
        num2 = int(state.pop())
        num1 = int(state.pop())
        state.append(num1 + num2)
    elif operator == '-':
        num2 = int(state.pop())
        num1 = int(state.pop())
        state.append(num1 - num2)
    elif operator == '~':
        num = int(state.pop())
        state.append(-num)
    elif operator == '!':
        num = int(state.pop())
        state.append(factorial(num))
    elif operator == '#':
        num = int(state.pop())
        state.append(num)
        state.append(num)
    elif operator == '@':
        num3 = int(state.pop())
        num2 = int(state.pop())
        num1 = int(state.pop())
        state.append(num2)
        state.append(num3)
        state.append(num1)


def main():
    state = []
    words = input().split(' ')

    for word in words:
        if word.isdigit():
            state.append(word)
        else:
            operator = word
            invoke_operation(operator, state)
    
    print(state[0])


if __name__ == '__main__':
    main()
