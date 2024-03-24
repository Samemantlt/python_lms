import re
from hashlib import sha256 


class MinLengthError(Exception):
    pass


class PossibleCharError(Exception):
    pass


class NeedCharError(Exception):
    pass


def password_validation(password, min_length=8, possible_chars=None, at_least_one=str.isdigit):
    if possible_chars is None:
        possible_chars = 'a-zA-Z0-9'
    else:
        possible_chars = re.escape(possible_chars)
    
    if not isinstance(password, str):
        raise TypeError()
    
    if len(password) < min_length:
        raise MinLengthError()

    if re.fullmatch(f'[{possible_chars}]*', password) is None:
        raise PossibleCharError()
    
    for symbol in password:
        if at_least_one(symbol):
            break
    else:
        raise NeedCharError()
    
    return sha256(password.encode('utf-8')).hexdigest()
