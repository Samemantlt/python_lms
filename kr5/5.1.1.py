class User:
    def __init__(self, name, birth, info):
        self.__name = name
        self.__birth = birth
        self.__info = info
    
    def get_login(self):
        return self.__name
    
    def get_birth_date(self):
        return self.__birth
    
    def get_info(self):
        return self.__info
