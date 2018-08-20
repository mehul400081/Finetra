

class Counter:

    value = 0

    def __int__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1