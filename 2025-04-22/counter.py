class Counter:
    def __init__(self, limit: int) -> None:
        self.count = 0
        self.limit = limit

    def inc(self) -> None:
        if self.count < self.limit:
            self.count += 1

    def get(self) -> int:
        return self.count

