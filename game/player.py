from locale import currency

class Player:
    def __init__(self, nid, name):
        self._id = nid
        self._name = name

    @property
    def pid(self):
        return self._id

    @property
    def name(self):
        return self._name

    def is_AI(self):
        return False

    def __str__(self):
        return self._name

    def __repr__(self):
        return f"Player({self._id}, '{self._name}')"


class BlackJackPlayer(Player):
    def __init__(self, nid, name, bankroll=10000):
        super().__init__(nid, name)
        self._balance = bankroll
        self._bet = 0
        # setlocale(LC_ALL, "en-US")

    @property
    def bankroll(self):
        return currency(self._balance, grouping=True)

    @property
    def bet(self):
        return currency(self._bet, grouping=True)

    @bet.setter
    def bet(self, wager):
        self._bet = wager

    def deduct_bet(self):
        self._balance = self._balance - self._bet

    def __repr__(self):
        return f"BlackJackPlayer({self._nid}, '{self._name}', bankroll={self._balance})"
