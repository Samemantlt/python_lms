roles = [
    'Junior',
    'Middle',
    'Senior',
]


def get_salary(role_index):
    salaries = [
        10,
        15,
        20
    ]
    if role_index < len(salaries):
        return salaries[role_index]

    return 20 + (role_index - len(salaries) + 1)


class Programmer:
    def __init__(self, name, role):
        self.name = name
        self.role_index = roles.index(role)
        self.worked = 0
        self.earned = 0

    def work(self, time):
        self.worked += time
        self.earned += get_salary(self.role_index) * time
    
    def rise(self):
        self.role_index += 1

    def info(self):
        return f'{self.name} {self.worked}ч. {self.earned}тгр.'
