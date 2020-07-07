class ParkingSession:
    def __init__(self, entryDt, carNumber, ticketNumber):
        self.__entryDt = entryDt
        self.__carNumber = carNumber
        self.__ticketNumber = ticketNumber
        self.__paymentDt = None
        self.__exitDt = None
        self.__totalPayment = None

    @property
    def entryDt(self):
        return self.__entryDt

    @property
    def carNumber(self):
        return self.__carNumber

    @property
    def ticketNumber(self):
        return self.__ticketNumber

    @property
    def paymentDt(self):
        return self.__paymentDt

    @paymentDt.setter
    def paymentDt(self, value):
        self.__paymentDt = value

    @property
    def exitDt(self):
        return self.__exitDt

    @exitDt.setter
    def exitDt(self, value):
        self.__exitDt = value

    @property
    def totalPayment(self):
        return self.__totalPayment

    @totalPayment.setter
    def totalPayment(self, value):
        self.__totalPayment = value


