"""Agglomerate prices"""


class RunIt:
    #TODO: Test for initial commit with new ssh key pair
    # TODO: merged the main with unrelated histories. does it work?

    def __init__(self):
        self.motors = 4
        self.props = None

    def set_motors(self, motors):
        self.motors = motors

    def set_props(self, props):
        self.props = props

