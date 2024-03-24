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


assert name_validation('Йеё')