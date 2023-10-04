class Buffer:
    def __init__(self):
        self.data = []

    def add(self, char):
        self.data.append(char)

    def get_next(self):
        return self.data.pop(0) if self.data else None

    def has_data(self):
        return bool(self.data)
            