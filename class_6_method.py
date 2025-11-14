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
    machine = WashingMachine(13, "Eve")
    machine.set_mode("Spin")
    return machine
