import itertools
import re
from typing import NamedTuple, List


priorities = [
    'not',
    'and',
    'or',
    '^',
    '->',
    '~',
]


def to_num(val):
    return 1 if val else 0


class Expression:
    def invoke(variables: dict) -> bool:
        pass

    def get_parameters(self) -> List['ParameterExpression']:
        pass


class ParameterExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def invoke(self, variables: dict) -> bool:
        return variables[self.name]
    
    def get_parameters(self) -> List['ParameterExpression']:
        return [self]


class NotExpression(Expression):
    def __init__(self, argument: Expression):
        self.argument = argument
    
    def invoke(self, variables: dict) -> bool:
        return not self.argument.invoke(variables)
    
    def get_parameters(self) -> List[ParameterExpression]:
        return [*self.argument.get_parameters()]


class AndExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def invoke(self, variables: dict) -> bool:
        return self.left.invoke(variables) and self.right.invoke(variables)
    
    def get_parameters(self) -> List[ParameterExpression]:
        return [*self.left.get_parameters(), *self.right.get_parameters()]


class OrExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def invoke(self, variables: dict) -> bool:
        return self.left.invoke(variables) or self.right.invoke(variables)
    
    def get_parameters(self) -> List[ParameterExpression]:
        return [*self.left.get_parameters(), *self.right.get_parameters()]


class XorExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def invoke(self, variables: dict) -> bool:
        return self.left.invoke(variables) ^ self.right.invoke(variables)
    
    def get_parameters(self) -> List[ParameterExpression]:
        return [*self.left.get_parameters(), *self.right.get_parameters()]


class ImplExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def invoke(self, variables: dict) -> bool:
        return self.left.invoke(variables) <= self.right.invoke(variables)
    
    def get_parameters(self) -> List[ParameterExpression]:
        return [*self.left.get_parameters(), *self.right.get_parameters()]


class EqualsExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right
    
    def invoke(self, variables: dict) -> bool:
        return self.left.invoke(variables) == self.right.invoke(variables)
    
    def get_parameters(self) -> List[ParameterExpression]:
        return [*self.left.get_parameters(), *self.right.get_parameters()]


RE_TOKENS = re.compile(r'\(|\)|(not)|(and)|(or)|\^|(\-\>)|\~|[A-Z]')


def parse_tokens(expression: str) -> list:
    tokens = []

    for match in RE_TOKENS.finditer(expression):
        token = match.group(0)
        tokens.append(token)
    
    return tokens


assert parse_tokens('A and B') == ['A', 'and', 'B']
assert parse_tokens('A or B') == ['A', 'or', 'B']
assert parse_tokens('not A or B') == ['not', 'A', 'or', 'B']
assert parse_tokens('not (A or B)') == ['not', '(', 'A', 'or', 'B', ')']
assert parse_tokens('(A -> B) ^ C') == ['(', 'A', '->', 'B', ')', '^', 'C']


class ExtraToken(NamedTuple):
    index: int
    value: str
    brackets_level: int


def parse_expression(expression: str) -> Expression:
    tokens = parse_tokens(expression)
    return parse_token_expression(tokens)


def parse_token_expression(tokens: List[str]) -> Expression:
    extra_tokens: List[ExtraToken] = [] 

    brackets_level = 0
    for i, token in enumerate(tokens):
        if token.isupper():
            continue

        if token == '(':
            brackets_level += 1
            continue
        elif token == ')':
            brackets_level -= 1
            continue
        
        op = ExtraToken(i, token, brackets_level)
        extra_tokens.append(op)

    if len(extra_tokens) == 0:
        for token in tokens:
            if token.isupper():
                return ParameterExpression(token)
    
    current_token = max(extra_tokens, key=lambda a: (-a.brackets_level, priorities.index(a[1]), a.index))

    if current_token.value == 'not':
        right = tokens[current_token.index + 1:]

        right_expression = parse_token_expression(right)

        return NotExpression(right_expression)

    if current_token.value == 'and':
        left = tokens[:current_token.index]
        right = tokens[current_token.index + 1:]

        left_expression = parse_token_expression(left)
        right_expression = parse_token_expression(right)

        return AndExpression(left_expression, right_expression)
    
    if current_token.value == 'or':
        left = tokens[:current_token.index]
        right = tokens[current_token.index + 1:]

        left_expression = parse_token_expression(left)
        right_expression = parse_token_expression(right)

        return OrExpression(left_expression, right_expression)
    
    if current_token.value == '^':
        left = tokens[:current_token.index]
        right = tokens[current_token.index + 1:]

        left_expression = parse_token_expression(left)
        right_expression = parse_token_expression(right)

        return XorExpression(left_expression, right_expression)
    
    if current_token.value == '->':
        left = tokens[:current_token.index]
        right = tokens[current_token.index + 1:]

        left_expression = parse_token_expression(left)
        right_expression = parse_token_expression(right)

        return ImplExpression(left_expression, right_expression)

    if current_token.value == '~':
        left = tokens[:current_token.index]
        right = tokens[current_token.index + 1:]

        left_expression = parse_token_expression(left)
        right_expression = parse_token_expression(right)

        return EqualsExpression(left_expression, right_expression)
    
    raise Exception(f'Unknown current token: {current_token}')


assert parse_token_expression(['A', 'and', 'B']).invoke({'A': True, 'B': True})
assert not parse_token_expression(['A', 'or', 'B']).invoke({'A': False, 'B': False})
assert parse_token_expression(['A', 'or', 'B']).invoke({'A': False, 'B': True})
assert not parse_expression('A and B').invoke({'A': True, 'B': False})
assert not parse_expression('not A and B').invoke({'A': True, 'B': False})
assert parse_expression('not (not A and B)').invoke({'A': True, 'B': False})


def main():
    values = [False, True]
    expression = input()

    parsed_expression = parse_expression(expression)
    parameters = parsed_expression.get_parameters()
    
    variable_names = set()
    for parameter in parameters:
        variable_names.add(parameter.name)
    
    variable_names = sorted(list(variable_names))

    print(' '.join(variable_names + ['F']))
    
    for current_values in itertools.product(values, repeat=len(variable_names)):
        local_variables = {variable_names[i]: current_values[i] for i in range(len(variable_names))}

        f = parsed_expression.invoke(local_variables)

        print(' '.join([str(to_num(i)) for i in list(current_values) + [f]]))


if __name__ == '__main__':
    main()
