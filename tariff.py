class Tariff:
    def __init__(self, minutes, rate):
        self.__minutes = minutes
        self.__rate = rate

    @property
    def minutes(self):
        return self.__minutes

    @property
    def rate(self):
        return self.__rate