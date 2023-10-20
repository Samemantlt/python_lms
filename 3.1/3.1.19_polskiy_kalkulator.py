def invoke_operation(operator: str, num1: int, num2: int):
    if operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2


def main():
    state = []
    words = input().split(' ')

    for word in words:
        if word.isdigit():
            state.append(word)
        else:
            operator = word
            num2 = int(state.pop())
            num1 = int(state.pop())
            result = invoke_operation(operator, num1, num2)
            state.append(result)
    
    print(state[0])


if __name__ == '__main__':
    main()
