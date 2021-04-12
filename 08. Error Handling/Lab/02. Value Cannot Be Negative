class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        self.value = value
        message = f"Value {value} is negative"
        super(ValueCannotBeNegativeError, self).__init__(message)


for _ in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegativeError(number)
