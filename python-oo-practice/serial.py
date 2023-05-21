"""Python serial number generator."""

class SerialGenerator():
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
    def __init__(self, start=0):
        '''generates new serial number, begins at given start value'''
        self.start = self.next = start
    
    def __repr__(self):
        '''describes SerialGenerator with start and next values'''
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        '''returns the next serial number value'''
        self.next += 1
        return self.next - 1
    
    def reset(self):
        '''resets the function, beginning again at the start value'''
        self.next = self.start

