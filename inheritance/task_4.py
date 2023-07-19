class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        self.log_error()

    def log_error(self):
        with open("logs.txt", "a") as log_file:
            log_file.write(self.msg + "\n")

try:
    raise CustomException("This is error")
except CustomException as e:
    pass