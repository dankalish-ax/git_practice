"""Get the prop stuff for the fake program """


class Prop:
    def __init__(self, diameter, pitch, num_blades, price):
        self.diameter = diameter
        self.pitch = pitch
        self.num_blades = num_blades
        self.price = price

    # TODO: more setters


    def get_diameter(self):
        return self.diameter

    def get_pitch(self):
        return self.pitch

    def get_num_blades(self):
        return self.num_blades

    def get_price(self):
        return self.price