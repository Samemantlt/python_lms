import re


class BadCharacterError(Exception):
    pass


class StartsWithDigitError(Exception):
    pass


def username_validation(name: str):
    if not isinstance(name, str):
        raise TypeError()
    
    if re.fullmatch('[a-zA-Z0-9_]*', name) is None:
        raise BadCharacterError()

    if len(name) >= 1 and name[0].isdigit():
        raise StartsWithDigitError()

    return name