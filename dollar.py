

class Dollar(object):

    def __init__(self, value):
        self._amount = value

    def times(self, value):
        self._amount *= value

    @property
    def amount(self):
        return self._amount
