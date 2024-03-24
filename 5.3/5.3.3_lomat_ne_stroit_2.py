class ErrorClass:
    def __repr__(self):
        raise Exception()
    
    def __str__(self):
        raise Exception()


func(ErrorClass())
