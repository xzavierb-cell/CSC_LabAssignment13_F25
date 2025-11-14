class WashingMachine:
    # class attributes
    brand = "Samsung"
    type = "Front Load"

    def __init__(self, capacity, owner):
        self.capacity = capacity  # kg
        self.owner = owner
        self.is_running = False
        self.mode = "Normal"

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def set_mode(self, mode):
        self.mode = mode


def test():
    # TODO: create one instance of class WashingMachine, send arguments: int value 13 and String value "Eve"
    # TODO: call method "set_mode()" and send argument "Spin"
    # TODO: return the instance
