# Not working


import datetime


class UserTypeError(TypeError):
    pass


class UserRecursionError(RecursionError):
    pass


class User:
    def __init__(self, name, birth, info):
        if type(name) is not str:
            raise TypeError
        if type(birth) is not str:
            raise TypeError
        if type(info) is not str:
            raise TypeError

        try:
            b = datetime.datetime.strptime(birth, '%d-%m-%Y')
        except Exception:
            raise ValueError
        
        if b > datetime.datetime.today():
            raise ValueError

        self.__name = name
        self.__birth = birth
        self.__info = info
        self.__confirmed = False
        self.__updated = False
        self.curator = None
    
    def get_login(self):
        return self.__name
    
    def get_birth_date(self):
        return self.__birth
    
    def get_info(self):
        return self.__info

    def confirm(self):
        self.__confirmed = True
    
    def is_confirmed(self):
        return self.__confirmed
    
    def edit_info(self, info):
        self.__info = info
        self.__updated = True

    def is_updated(self):
        return self.__updated
    
    def get_staff(self):
        return self.curator

    def __rshift__(self, other):
        if type(other) is not StaffUser:
            raise UserTypeError
        other.add_ward(self)
    
    def __gt__(self, other):
        if self.curator == other:
            return True
        if self.curator is None:
            return False
        return self.curator > other
    
    def __lt__(self, other):
        if other.curator == self:
            return True
        if other.curator is None:
            return False
        return self < other.curator

    def __repr__(self):
        return f"User({self.get_login()}, {self.get_birth_date()}, {repr(self.curator)})"

    def __str__(self):
        return f"{self.get_login()} ({self.get_birth_date()}):\n{self.get_info()}\n"


class StaffUser(User):
    def __init__(self, name, birth):
        User.__init__(self, name, birth, 'Staff User')
        self.__wards = []

    def add_ward(self, user):
        if type(user) not in [User, StaffUser]:
            raise UserTypeError
        
        if self > user:
            raise UserRecursionError
        
        if type(self) is not StaffUser:
            raise UserTypeError

        self.__wards.append(user)
        user.curator = self
    
    def get_wards(self):
        return self.__wards

    def __repr__(self):
        return f"StaffUser({self.get_login()}, {self.get_birth_date()})"


a = User('asd', '12-02-2023', '123')
b = StaffUser('asd2', '12-02-2023')
b.add_ward(a)