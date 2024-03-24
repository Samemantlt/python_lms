try:
    func()
except Exception as ex:
    print(type(ex).__name__)
else:
    print("No Exceptions")