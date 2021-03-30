

class Transaction:
    def __init__(self, trade_id=None, trade_time=None, price=None,
                    quantity=None, who=None):
        self.trade_id = trade_id
        self.trade_time = trade_time
        self.price=price
        self.quantity = quantity
        self.who = who

    def __repr__(self):
        return "%s" % (self.price)

    def __eq__(self, other):
        return self.trade_id == other.trade_id

    def __hash__(self):
        return int(self.trade_id)