class User:
    def __init__(self, name, birth, info):
        self.__name = name
        self.__birth = birth
        self.__info = info
        self.__confirmed = False
        self.__updated = False
    
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

    def __str__(self):
        return f"{self.get_login()} ({self.get_birth_date()}):\n{self.get_info()}\n"
