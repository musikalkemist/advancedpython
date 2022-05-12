class CurrencyError(Exception):

    def __init__(self, currency: str, message: str) -> None:
        self.currency = currency
        self.message = message


class DifferentNumberOfArgumentsError(Exception):

    def __init__(self, message: str) -> None:
        self.message = message