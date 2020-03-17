"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.


    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        "Creates a machine that accepts a starting serial number"
        self.start = start
        self.increment = start - 1

    def __repr__(self):
        return f"<SerialGenerator start = {self.start}>"

    def generate(self):
        "Generates a new serial number (starting/current number) plus one"
        self.increment += 1
        return self.increment

    def reset(self):
        "Resets the counting number to the start number provided or 100"
        self.increment = self.start - 1
