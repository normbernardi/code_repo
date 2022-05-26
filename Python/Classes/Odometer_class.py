def is_ascending(n: int) -> bool:
    return all(a < b for a, b in zip(str(n), str(n)[1:]))


class Odometer:
    def __init__(self, size):
        self.SIZE = size
        self.START = int('123456789'[:size])
        self.LIMIT = int('123456789'[-size:])
        self.read = self.START

    def __str__(self):
        return str(self.read)

    def __repr__(self):
        return f'{self.START}<<{self.read}>>{self.LIMIT}'

    def set_reading(self, n: int):
        self.read = n
        pass

    def after(self, step=1):
        for _ in range(step):
            if self.read == self.LIMIT:
                self.read == self.START
            else:
                self.read += 1
                while not is_ascending(self.read):
                    self.read += 1

    def before(self, step=1):
        for _ in range(step):
            if self.read == self.START:
                self.read == self.LIMIT
            else:
                self.read -= 1
                while not is_ascending(self.read):
                    self.read -= 1

    def next(self):
        if not is_ascending(self.read):
            return -1
        if self.read == self.LIMIT:
            self.read = self.START
            return self.read
        self.read += 1
        while not is_ascending(self.read):
            self.read += 1
        return self.read

    def prev(self):
        if not is_ascending(self.read):
            return -1
        if self.read == self.START:
            self.read = self.LIMIT
            return self.read
        self.read -= 1
        while not is_ascending(self.read):
            self.read -= 1
        return self.read

    def distance(self, other):
        if self.SIZE != other.SIZE:
            return -1
        diff = 0
        lower, upper = min(self.read, other.read), max(self.read, other.read)
        while not lower == upper:
            diff += 1
            lower += 1
            while not is_ascending(lower):
                lower += 1
        return diff




