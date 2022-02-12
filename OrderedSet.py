class OrderedSet:
    def __init__(self):
        self.dict = {}

    def add(self, item):
        self.dict[item] = None

    def __iter__(self):
        return iter(self.dict)

        