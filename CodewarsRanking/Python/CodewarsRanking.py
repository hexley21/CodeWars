class User:
    __slots__ = '__rank', '__progress'
    allowed = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.__rank = -8
        self.__progress = 0

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        if rank == 8:
            self.__progress = 0
        if rank in self.allowed:
            self.__rank = rank
        else:
            raise TypeError("rank should be in range of -8 and 9, skipping 0")

    @property
    def progress(self):
        return self.__progress

    @progress.setter
    def progress(self, progress):
        gain = (progress) // 100
        self.__progress = progress - (100 * (progress // 100))
        if self.__rank + gain >= 8:
            self.rank = 8
        elif self.__rank + gain == 0:
            self.rank = 1
        else:
            self.rank = self.allowed[self.allowed.index(self.rank) + gain]

    def inc_progress(self, lvl):
        d = self.allowed.index(lvl) - self.allowed.index(self.__rank)
        if d <= -2:
            d = 0
        elif d == -1:
            d = 1
        elif d == 0:
            d = 3
        else:
            d *= d * 10
        self.progress += d
