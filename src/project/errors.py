class CurrencyError(Exception):

    def __int__(self, currency: str, message: str) -> None:
        self.currency = currency
        self.message = message


class DifferentNumberOfArgumentsError(Exception):

    def __int__(self, message: str) -> None:
        self.message = message