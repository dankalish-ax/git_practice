"""The motor class for this thing """


class Motors:
    def __init__(self, stator, kv, size, price):
        self.stator = stator
        self.kv = kv
        self.size = size
        self.price = price

    def set_stator(self, new_stator):
        self.stator = new_stator

    def set_kv(self, new_kv):
        self.kv = new_kv

    # TODO: add more setters

    def get_stator(self):
        return self.stator

    def get_kv(self):
        return self.kv

    def get_size(self):
        return self.size

    def get_price(self):
        return self.price
