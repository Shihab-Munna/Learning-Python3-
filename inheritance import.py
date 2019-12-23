class CustomError (Exception):
    def __init__(self,message):
        self.message = message

try:
    raise CustomError('Is is an Custom Error')
except CustomError as e:
    print(e)

