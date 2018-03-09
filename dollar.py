

class Dollar(object):

    def __init__(self, amount):
        self._amount = amount

    def times(self, multiple):
        return Dollar(self._amount * multiple)

    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
