
class TerminalScribeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidParameterException(TerminalScribeException):
    pass