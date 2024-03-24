import re


class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(name: str):
    if not isinstance(name, str):
        raise TypeError()

    if re.fullmatch('[А-Яа-яёЁ]*', name) is None:
        raise CyrillicError()
    
    if len(name) >= 1 and name[0].islower():
        raise CapitalError()
    
    for symbol in name[1:]:
        if symbol.isupper():
            raise CapitalError()
    
    return name


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


def user_validation(**kwargs):
    if len(kwargs) != 3:
        raise KeyError()
    if 'first_name' not in kwargs:
        raise KeyError()
    if 'last_name' not in kwargs:
        raise KeyError()
    if 'username' not in kwargs:
        raise KeyError()
    
    if not isinstance(kwargs['first_name'], str):
        raise TypeError
    if not isinstance(kwargs['last_name'], str):
        raise TypeError
    if not isinstance(kwargs['username'], str):
        raise TypeError

    name_validation(kwargs['last_name'])
    name_validation(kwargs['first_name'])
    username_validation(kwargs['username'])

    return kwargs