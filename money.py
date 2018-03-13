def dollar(value):
    return create_currency(value=value, currency='USD')


def franc(value):
    return create_currency(value, currency='CHF')


def create_currency(value, currency):
    return Money(value=value, currency=currency)


class MoneyTypeError(TypeError):
    pass


class Money(object):
    def __init__(self, value, currency):
        self._value = value
        self._currency = currency

    def times(self, multiple):
        return create_currency(self.amount * multiple, currency=self.currency)

    @property
    def amount(self):
        return self._value

    @property
    def currency(self):
        return self._currency

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ and self.currency == other.currency

    def __add__(self, other):
        if self.currency == other.currency:
            value = self.amount + other.amount
            return create_currency(value=value, currency=self.currency)
        else:
            raise MoneyTypeError('different currencies')

    def plus(self, other):
        if self.currency == other.currency:
            return create_currency(value=self.amount + other.amount, currency=self.currency)
        else:
            raise MoneyTypeError('different currencies')

